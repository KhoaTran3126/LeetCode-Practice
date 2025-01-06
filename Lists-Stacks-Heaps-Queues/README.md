# Lists, Stacks, Heaps, Queues
Contain problems involving lists, stacks, heaps, and queues.

## Singly Linked List:
<pre>
  <code>
class SinglyNode:
  data __init__(self, data=None):
    self.data = data
    self.next = None
  </code>

def insert_begin(head, new_data):
  new_data = SinglyNode(new_data)
  new_data.next = head
  return new_data
  
def insert_begin(head, new_data):
  new_data = SinglyNode(new_data)
  curr = head
  while curr.next is not None:
    curr = curr.next
  curr.next = new_data
  return head

def inert_after_given_node(given_node, new_data):
  new_data = SinglyNode(new_data)
  new_data.next = given_node.next
  given_node.next = new_data
</pre>
