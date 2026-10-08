
########################################
ament_cmake_core.core/list_append_unique
########################################

.. module:: ament_cmake_core.core/list_append_unique


.. function:: list_append_unique(list)

   Append elements to a list if they are not already in the list.
   
   :param list: the list
   :type list: list variable
   :param ARGN: the elements
   :type ARGN: list of strings
   
   .. note:: Using CMake's ``list(APPEND ..)`` and
     ``list(REMOVE_DUPLICATES ..)`` is not sufficient since its
     implementation uses a set internally which makes the operation
     unstable.
   

