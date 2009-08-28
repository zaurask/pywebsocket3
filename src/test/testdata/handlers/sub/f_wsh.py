# Copyright 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Exception in web_socket_transfer_data().
"""


def web_socket_shake_hands(conn_context):
    pass


def web_socket_transfer_data(conn_context):
    raise Exception('Intentional Exception for %s, %s' %
                    (conn_context.resource, conn_context.protocol))


# vi:sts=4 sw=4 et