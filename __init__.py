# Anki Translator Add-on
# Helps creating vocabulary flashcards by searching for translations on the web.
#
# https://github.com/jannewulf/Anki-Translator
# jannewulf@gmail.com
#
# Copyright (C) 2016 Janne Wulf https://github.com/jannewulf https://github.com/jannewulf/Anki-Translator
#               2020 Xaver Kainz https://github.com/XKainz https://github.com/XKainz/Anki-Translator
#               2022 naota1 https://github.com/naota1 https://github.com/naota1/Anki-Translator
#               2022 Alex Archer https://github.com/alexarcherr https://github.com/alexarcherr/Anki-Translator/
#               2024 Shigeyuki http://patreon.com/Shigeyuki
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from . import TranslatorAddon

# Here you can set the default Languages.
# For available Language Codes you can see TranslatorAddon/Parser/pons_lang_codes.xml
TranslatorAddon.defaultSourceLanguage = "de"
TranslatorAddon.defaultTargetLanguage = "en"
TranslatorAddon.defaultLoadGrammarInfos = True

TranslatorAddon.__init__()
