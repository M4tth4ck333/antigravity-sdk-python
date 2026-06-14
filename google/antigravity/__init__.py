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

"""Google Antigravity SDK for building AI agents."""

from google.antigravity.agent import Agent
from google.antigravity.connections.connection import AgentConfig
from google.antigravity.connections.local.local_connection_config import LocalAgentConfig
from google.antigravity.tools.tool_context import ToolContext
from google.antigravity.types import CapabilitiesConfig
from google.antigravity.types import GeminiAPIEndpoint
from google.antigravity.types import GeminiConfig
from google.antigravity.types import GeminiModelOptions
from google.antigravity.types import GenerationConfig
from google.antigravity.types import ModelConfig
from google.antigravity.types import ModelEndpoint
from google.antigravity.types import ModelEntry
from google.antigravity.types import ModelTarget
from google.antigravity.types import ModelType
from google.antigravity.types import ThinkingLevel
from google.antigravity.types import UsageMetadata
from google.antigravity.types import VertexEndpoint

__all__ = [
    "Agent",
    "AgentConfig",
    "LocalAgentConfig",
    "ToolContext",
    "CapabilitiesConfig",
    "GeminiAPIEndpoint",
    "GeminiConfig",
    "GenerationConfig",
    "ModelConfig",
    "ModelTarget",
    "ModelEndpoint",
    "ModelEntry",
    "GeminiModelOptions",
    "ModelType",
    "ThinkingLevel",
    "UsageMetadata",
    "VertexEndpoint",
]
