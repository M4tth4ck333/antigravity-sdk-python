# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Trigger system for the Antigravity SDK.

Triggers are long-lived async functions that run alongside an agent
session, react to external events (cron, file changes, webhooks),
and push messages back into the agent.

Import from the specific submodule you need::

    from google.antigravity.triggers import triggers
    from google.antigravity.triggers import trigger_runner
    from google.antigravity.triggers import helpers
"""
