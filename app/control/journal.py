

from typing import List
from app.control.models import CommandJournalEntry




class CommandJournal:
    def __init__(self):
        self._entries: List[CommandJournalEntry] = []

    def append(self, entry: CommandJournalEntry) -> None:
        self._entries.append(entry)

    def get_all(self) -> List[CommandJournalEntry]:
        return self._entries.copy()


journal = CommandJournal()
