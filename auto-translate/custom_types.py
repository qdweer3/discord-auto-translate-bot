from typing import Dict
from typing import List
from typing import Tuple
from enum import Enum

# As ISO-639-1 code (used by google translate)
class Language(Enum):
    ENGLISH = 'en'
    RUSSIAN = 'ru'

Name = str
Id = int
Server = Tuple[Name, Id]
Channel = Tuple[Name, Id]
SourceChannel = Tuple[Channel, Language]
TargetChannel = Tuple[Channel, Language]
Link = Dict[SourceChannel, List[TargetChannel]]
ServerLinks = Dict[Server, List[Link]]