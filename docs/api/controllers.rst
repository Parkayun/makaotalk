makaotalk.controllers
=====================


makaotalk.controllers.web
-------------------------

.. automodule:: makaotalk.controllers.web
   :members:



makaotalk.controllers.websocket
-------------------------------

.. automodule:: makaotalk.controllers.websocket
   :members:

   .. autofunction:: makaotalk.controllers.websocket.chat(data)

      Websocket controller when users doing real-time chat.
      Save chat messages on db and broadcast them each others who joined chat room.

      :param data: Data dictionary of chat.

         - `username`: Message author's username.
         - `message`: Message content.
         - `room`: primary key of :class:`~makaotalk.models.chat.ChatRoom`.

      :type data: :class:`dict`


   .. autofunction:: makaotalk.controllers.websocket.delete(data)

      Websocket controller when users delete their own message.
      Delete chat message on db and broadcast each others who joined chat room.

      :param data: Data dictionary of chat.

         - `message_id`: primary key of :class:`~makaotalk.models.chat.Message`.
         - `room`: primary key of :class:`~makaotalk.models.chat.ChatRoom`.

      :type data: :class:`dict`


   .. autofunction:: makaotalk.controllers.websocket.join(data)

      Websocket controller when users joined chat room.
      Doing join logic with specific chat room.

      :param data: Data dictionary of chat.

         - `username`: Message author's username.
         - `room`: primary key of :class:`~makaotalk.models.chat.ChatRoom`.

      :type data: :class:`dict`


   .. autofunction:: makaotalk.controllers.websocket.update(data)

      Websocket controller when users modify their own message.
      Update chat message on db and broadcast each others who joined chat room.

      :param data: Data dictionary of chat.

         - `username`: Message author's username.
         - `message_id`: primary key of :class:`~makaotalk.models.chat.Message`.
         - `message`: Message content.
         - `room`: primary key of :class:`~makaotalk.models.chat.ChatRoom`.

      :type data: :class:`dict`
