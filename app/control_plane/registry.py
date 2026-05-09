from typing import Dict, List
from app.control_plane.models import CommandDefinition
from app.control_plane.enums import CommandClass
from app.control_plane.exceptions import InvalidCommandDefinitionError
from app.control_plane.commands import DEFAULT_COMMANDS


class CommandRegistry:
    def __init__(self):
        self._commands: Dict[CommandClass, CommandDefinition] = {}
        for cmd in DEFAULT_COMMANDS:
            self.register(cmd)

    def register(self, command: CommandDefinition):
        if command.command_id in self._commands:
            raise InvalidCommandDefinitionError(
                f"Duplicate command {command.command_id}"
            )
        self._commands[command.command_id] = command

    def get_command(self, command_id: CommandClass) -> CommandDefinition:
        if command_id not in self._commands:
            raise InvalidCommandDefinitionError(f"Command not found {command_id}")
        return self._commands[command_id]

    def list_commands(self) -> List[CommandDefinition]:
        return list(self._commands.values())
