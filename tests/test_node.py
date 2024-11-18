from src.node import Node, NodeType


def test_create_node():
  node1 = Node(NodeType.INT, value=1, name='1')
  node2 = Node(NodeType.FLOAT, value=1.0, name='1.0')
  node = Node(NodeType.NOT_TOKEN, name='root', children=[node1, node2])

  assert node.type == NodeType.NOT_TOKEN
  assert node.name == 'root'
  assert node.children == [node1, node2]
  assert node.value is None

  assert node1.type == NodeType.INT
  assert node1.name == '1'
  assert node1.value == 1
  assert node1.children == []

  assert node2.type == NodeType.FLOAT
  assert node2.name == '1.0'
  assert node2.value == 1.0
  assert node2.children == []

  node3 = Node(NodeType.ERROR)
  assert node3.type == NodeType.ERROR
  assert node3.name is None
  assert node3.value is None
  assert node3.children == []

  node4 = Node(NodeType.VOID)
  assert node4.type == NodeType.VOID
  assert node4.name is None
  assert node4.value is None
  assert node4.children == []

  node5 = Node(NodeType.STRING, value='hello')
  assert node5.type == NodeType.STRING
  assert node5.name is None
  assert node5.value == 'hello'
  assert node5.children == []

  node6 = Node(NodeType.JSON, value={'a': 1})
  assert node6.type == NodeType.JSON
  assert node6.name is None
  assert node6.value == {'a': 1}
  assert node6.children == []

  node7 = Node(NodeType.TOKEN, name='token')
  assert node7.type == NodeType.TOKEN
  assert node7.name == 'token'
  assert node7.value is None
  assert node7.children == []

  node8 = Node(NodeType.NOT_TOKEN, name='root', children=[node1, node2])
  assert node8.type == NodeType.NOT_TOKEN
  assert node8.name == 'root'
  assert node8.children == [node1, node2]
  assert node8.value is None

  node9 = Node(NodeType.NOT_TOKEN, name='root', children=[node1, node2])
  assert node9.type == NodeType.NOT_TOKEN
  assert node9.name == 'root'
  assert node9.children == [node1, node2]
  assert node9.value is None

