# Stubs for marathon.client (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .models import MarathonApp as MarathonApp, MarathonDeployment as MarathonDeployment, MarathonGroup as MarathonGroup, MarathonInfo as MarathonInfo, MarathonTask as MarathonTask, MarathonEndpoint as MarathonEndpoint, MarathonQueueItem as MarathonQueueItem
from .exceptions import InternalServerError as InternalServerError, NotFoundError as NotFoundError, MarathonHttpError as MarathonHttpError, MarathonError as MarathonError
from .models.events import EventFactory as EventFactory
from .util import MarathonJsonEncoder as MarathonJsonEncoder, MarathonMinimalJsonEncoder as MarathonMinimalJsonEncoder

class MarathonClient:
    session = ...  # type: Any
    servers = ...  # type: Any
    auth = ...  # type: Any
    verify = ...  # type: Any
    timeout = ...  # type: Any
    auth_token = ...  # type: Any
    def __init__(self, servers, username: Optional[Any] = ..., password: Optional[Any] = ..., timeout: int = ..., session: Optional[Any] = ..., auth_token: Optional[Any] = ..., verify: bool = ...) -> None: ...
    def list_endpoints(self): ...
    def create_app(self, app_id, app): ...
    def list_apps(self, cmd: Optional[Any] = ..., embed_tasks: bool = ..., embed_counts: bool = ..., embed_deployments: bool = ..., embed_readiness: bool = ..., embed_last_task_failure: bool = ..., embed_failures: bool = ..., embed_task_stats: bool = ..., app_id: Optional[Any] = ..., **kwargs): ...
    def get_app(self, app_id, embed_tasks: bool = ..., embed_counts: bool = ..., embed_deployments: bool = ..., embed_readiness: bool = ..., embed_last_task_failure: bool = ..., embed_failures: bool = ..., embed_task_stats: bool = ...): ...
    def restart_app(self, app_id, force: bool = ...): ...
    def update_app(self, app_id, app, force: bool = ..., minimal: bool = ...): ...
    def update_apps(self, apps, force: bool = ..., minimal: bool = ...): ...
    def rollback_app(self, app_id, version, force: bool = ...): ...
    def delete_app(self, app_id, force: bool = ...): ...
    def scale_app(self, app_id, instances: Optional[Any] = ..., delta: Optional[Any] = ..., force: bool = ...): ...
    def create_group(self, group): ...
    def list_groups(self, **kwargs): ...
    def get_group(self, group_id): ...
    def update_group(self, group_id, group, force: bool = ..., minimal: bool = ...): ...
    def rollback_group(self, group_id, version, force: bool = ...): ...
    def delete_group(self, group_id, force: bool = ...): ...
    def scale_group(self, group_id, scale_by): ...
    def list_tasks(self, app_id: Optional[Any] = ..., **kwargs): ...
    def kill_given_tasks(self, task_ids, scale: bool = ..., force: Optional[Any] = ...): ...
    def kill_tasks(self, app_id, scale: bool = ..., wipe: bool = ..., host: Optional[Any] = ..., batch_size: int = ..., batch_delay: int = ...): ...
    def kill_task(self, app_id, task_id, scale: bool = ..., wipe: bool = ...): ...
    def list_versions(self, app_id): ...
    def get_version(self, app_id, version): ...
    def list_event_subscriptions(self): ...
    def create_event_subscription(self, url): ...
    def delete_event_subscription(self, url): ...
    def list_deployments(self): ...
    def list_queue(self): ...
    def delete_deployment(self, deployment_id, force: bool = ...): ...
    def get_info(self): ...
    def get_leader(self): ...
    def delete_leader(self): ...
    def ping(self): ...
    def get_metrics(self): ...
    def event_stream(self, raw: bool = ...): ...
