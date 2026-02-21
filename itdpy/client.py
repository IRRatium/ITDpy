from __future__ import annotations

from typing import Any
import time
import random
import requests
from requests import Response
from .auth import AuthManager
from .api import (
    create_post, 
    delete_post, 
    get_post, 
    get_posts, 
    get_user_posts, 
    like_post, 
    repost_post, 
    unlike_post, 
    update_post, 
    create_comment, 
    delete_comment, 
    get_comments,
    like_comment,
    reply_to_comment,
    unlike_comment,
    follow_user,
    get_followers,
    get_following,
    get_me,
    get_user,
    unfollow_user,
    get_notifications,
    mark_all_notification_read,
    mark_notification_read,
    get_top_clans,
    upload_file,
    update_profile,
    get_replies,
    get_pins,
    set_pin, 
    remove_pin,
    vote,
    who_to_follow,
    search_hashtags,
    search,
    update_notification_settings,
    update_privacy,
    get_trending_hashtags,
)
from .models import *

class ITDClient:
    ######################################################
    ############  Низкоуровневые методы API #############№
    ######################################################
    
    _DEFAULT_TIMEOUT = 15
    _UPLOAD_TIMEOUT = 3600
    _SDK_NAME = "itdpy"
    _SDK_VERSION = "0.3.2"
    _PLATFORM = "python"

    def __init__(self, refresh_token: str, auto_auth: bool = True):
        self.base_url = "https://xn--d1ah4a.com"
        self.session = requests.Session()

        self._access_token: str | None = None
        self._user_id: str | None = None
        self._auth_manager: Any = None

        self.session.headers.update(
            {
                "Origin": self.base_url,
                "Referer": f"{self.base_url}/",
            }
        )

        self.session.cookies.set(
            name="refresh_token",
            value=refresh_token,
            domain="xn--d1ah4a.com",
            path="/api",
        )

        self._apply_user_agent(initial=True)
        if auto_auth:
            from .auth import AuthManager
            auth = AuthManager(self)
            self._bind_auth_manager(auth)
            auth.refresh_access_token()

    @property
    def access_token(self) -> str | None:
        return self._access_token

    @property
    def user_id(self) -> str | None:
        return self._user_id

    def _bind_auth_manager(self, auth_manager: Any) -> None:
        self._auth_manager = auth_manager

    def _set_access_token(self, token: str) -> None: 
        self._access_token = token 
        self.session.headers["Authorization"] = f"Bearer {token}"

    def _set_user_id(self, user_id: str) -> None:
        self._user_id = user_id
        self._apply_user_agent()

    def _build_user_agent(self, initial: bool = False) -> str:
        if initial or not self._user_id:
            return (
                f"{self._SDK_NAME}/{self._SDK_VERSION} "
                f"(initial; platform={self._PLATFORM})"
            )
        return (
            f"{self._SDK_NAME}/{self._SDK_VERSION} "
            f"(userid={self._user_id}; platform={self._PLATFORM})"
        )

    def _apply_user_agent(self, initial: bool = False) -> None:
        self.session.headers["User-Agent"] = self._build_user_agent(initial)

    def _request(
        self,
        method: str,
        path: str,
        *,
        retry: bool = True,
        retries: int = 3,
        **kwargs: Any
    ) -> Response:

        self._apply_user_agent()

        if not path.startswith("/"):
            path = f"/{path}"

        url = f"{self.base_url}{path}"

        timeout = kwargs.pop("timeout", None)
        if timeout is None:
            timeout = (
                self._UPLOAD_TIMEOUT
                if path.startswith("/api/files")
                else self._DEFAULT_TIMEOUT
            )

        attempt = 0

        while True:
            response = self.session.request(method, url, timeout=timeout, **kwargs)

        
            if response.status_code == 401 and retry and self._auth_manager:
                refreshed = self._auth_manager.refresh_access_token()
                if refreshed:
                    retry = False
                    continue

            if response.status_code == 429 and attempt < retries:
                print("Rate limit reached. Waiting 5 seconds...")
                time.sleep(5)
                attempt += 1
                continue

            return response

    def get(self, path: str, **kwargs: Any) -> Response:
        return self._request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> Response:
        return self._request("POST", path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> Response:
        return self._request("PUT", path, **kwargs)

    def patch(self, path: str, **kwargs: Any) -> Response:
        return self._request("PATCH", path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> Response:
        return self._request("DELETE", path, **kwargs)
    

    ######################################################
    ############  Высокоуровневые методы API #############
    ######################################################

    def create_comment(
        self,
        post_id: str,
        content: str,
        attachment_ids: list[str] | str | None = None,
        parse_html: bool = False,
    ) -> Comment:
        return create_comment(self, post_id, content, attachment_ids, parse_html)

    def reply_to_comment(
        self,
        comment_id: str,
        content: str,
        attachment_ids: list[str] | str | None = None,
    )  -> Comment:
        return reply_to_comment(self, comment_id, content, attachment_ids)
    
    def delete_comment(self, comment_id: str) -> bool:
        return delete_comment(self, comment_id)
    
    def like_comment(self, comment_id: str) -> bool:
        return like_comment(self, comment_id)
    
    def unlike_comment(self, comment_id: str) -> bool:
        return unlike_comment(self, comment_id)

    def get_comments(self, post_id: str, limit: int = 20, sort: str = "popular") -> Comments:
        return get_comments(self, post_id, limit, sort)
    
    def upload_file(self, file_path):
        return upload_file(self, file_path)
    
    def get_top_clans(self):
        return get_top_clans(self)
    
    def get_notifications(self, offset: int = 0, limit: int = 20) -> Notifications:
        return get_notifications(self, offset, limit)
    
    def mark_notification_read(self, notification_id) -> bool:
        return mark_notification_read(self, notification_id)
    
    def mark_all_notification_read(self, notification_ids):
        return mark_notification_read(self, notification_ids)
    
    def get_posts(self, limit: int = 20, tab: str = "popular", cursor: int = 1 ) -> Posts:
        return get_posts(self, limit, tab, cursor)
    
    def get_post(self, post_id: str) -> Post:
        return get_post(self, post_id)
    
    def create_post(
        self,
        content: str = "",
        attachment_ids: list[str] | str | None = None,
        wall_recipient_id: str | None = None,
        poll: dict | Poll | None = None,
        parse_html: bool = False,
    ) -> Post:
        return create_post(self, content, attachment_ids, wall_recipient_id, poll, parse_html)
    
    def update_post(self, post_id: str, content: str, parse_html: bool = False) -> dict:
        return update_post(self, post_id, content, parse_html)
    
    def delete_post(self, post_id: str) -> bool:
        return delete_post(self, post_id)
    
    def like_post(self, post_id: str) -> bool:
        return like_post(self, post_id)
    
    def unlike_post(self, post_id: str) -> bool:
        return unlike_post(self, post_id)
    
    def repost_post(self, post_id: str, content: str | None = None) -> bool:
        return repost_post(self, post_id, content)
    
    def get_user_posts(self, username: str, limit: int = 20, sort: str = "new",  cursor: str | None = None) -> Posts:
        return get_user_posts(self, username, limit, sort, cursor)
    
    def update_profile(
    self,
    *,
    display_name: str | None = None,
    username: str | None = None,
    bio: str | None = None,
    banner_id: str | None = None,
    ) -> Me:
        return update_profile(self, display_name=display_name, username=username, bio=bio, banner_id=banner_id)
    
    def get_me(self) -> Me:
        return get_me(self)
    
    def get_user(self, username: str) -> User:
        return get_user(self, username)
    
    def follow_user(self, username: str) -> bool:
        return follow_user(self, username)
    
    def unfollow_user(self, username: str) -> bool:
        return unfollow_user(self, username)
    
    def get_followers(self, username: str, page: int = 1, limit: int = 30) -> Users:
        return get_followers(self, username, page, limit)
    
    def get_following(self, username: str, page: int = 1, limit: int = 30) -> Users:
        return get_following(self, username, page, limit)

    def get_replies(self, comment_id: str, sort = "newest"):
        return get_replies(self, comment_id, sort)
    
    def get_pins(self):
        return get_pins(self)
    
    def remove_pin(self):
        return remove_pin(self)
    
    def set_pin(self, slug):
        return set_pin(self, slug)
    
    def vote(self, post_id, option_ids):
        return vote(self, post_id, option_ids)
    
    def who_to_follow(self):
        return who_to_follow(self)
    
    def search_hashtags(self, name, limit = 20):
        return search_hashtags(self, name, limit)
    
    def search(self, query, user_limit = 5, hashtag_limit = 5):
        return search(self, query, user_limit, hashtag_limit)
    
    def update_privacy(
        self,
        *,
        is_private: bool | None = None,
        wall_access: str | None = None,
        likes_visibility: str | None = None,
        show_last_seen: bool | None = None,
    ):
        return update_privacy(
        self,
        is_private=is_private,
        wall_access=wall_access,
        likes_visibility=likes_visibility,
        show_last_seen=show_last_seen,
    )

    def update_notification_settings(
        self,
        *,
        enabled: bool | None = None,
        comments: bool | None = None,
        follows: bool | None = None,
        likes: bool | None = None,
        mentions: bool | None = None,
        sound: bool | None = None,
        wall_posts: bool | None = None,
    ):
        return update_notification_settings(self, enabled=enabled, comments=comments, follows=follows, likes=likes, mentions=mentions, sound=sound, wall_posts=wall_posts)
    
    def get_trending_hashtags(self, limit: int = 10):
        return get_trending_hashtags(self, limit)