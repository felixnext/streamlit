# -*- coding: utf-8 -*-
# Copyright 2018-2019 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""exception_proto Unittest."""

import unittest

from streamlit.elements.exception_proto import _format_syntax_error_message


class ExceptionProtoTest(unittest.TestCase):
    def test_format_syntax_error_message(self):
        """Tests that format_syntax_error_message produces expected output"""
        err = SyntaxError(
            'invalid syntax',
            ('syntax_hilite.py', 84, 23, 'st.header(header_text))\n'))

        expected = """
File "syntax_hilite.py", line 84
  st.header(header_text))
                        ^
SyntaxError: invalid syntax
"""
        self.assertEqual(expected.strip(), _format_syntax_error_message(err))
