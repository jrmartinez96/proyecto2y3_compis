import sys

class Node:
    def __init__(self, id, isInitial, isFinal):
        self.id = id
        self.isInitial = isInitial
        self.isFinal = isFinal

class Link:
    def __init__(self, source, target, label):
        self.source = source
        self.target = target
        self.label = label

def separate_words(fileRead):
    words = []
    currentWord = ''
    for character in fileRead:
        if character != " ":
            currentWord = currentWord + character
        else:
            if len(currentWord) != 0:
                words.append(currentWord)
                currentWord = ""
    
    if currentWord != "":
        words.append(currentWord)
    
    return words

def test_word(word, nodes, links):
    initialStates = []
    acceptStates = []

    for node in nodes:
        if node.isInitial:
            initialStates.append(node)
        if node.isFinal:
            acceptStates.append(node)
    
    itBelongs = False

    # recorrer los estados iniciales
    for initialState in initialStates:
        currentState = initialState

        # verificar cada letra de la palabra en el afd
        for iWord in range(len(word)):
            letter = word[iWord]

            currentState = evaluate_character(letter, currentState, nodes, links)

            if (currentState == -1):
                break
            else:
                if iWord == (len(word) - 1):
                    if currentState.isFinal:
                        itBelongs = True
    
    return itBelongs

def link_exists(word, nodes, links):
    initialStates = []
    acceptStates = []

    for node in nodes:
        if node.isInitial:
            initialStates.append(node)
        if node.isFinal:
            acceptStates.append(node)
    
    linkExists = True

    # recorrer los estados iniciales
    for initialState in initialStates:
        currentState = initialState

        # verificar cada letra de la palabra en el afd
        for iWord in range(len(word)):
            letter = word[iWord]

            currentState = evaluate_character(letter, currentState, nodes, links)

            if (currentState == -1):
                linkExists = False
                break
            else:
                linkExists = True
    
    return linkExists

def isNumber():
    return True

def isDecNumber():
    return False

# Devuelve -1 si no existe transicion desde el nodo hacia otro con la letter, de lo contrario devuelve el nodo target
def evaluate_character(letter, currentState, nodes, links):
    initialState = currentState
    stateId = -1

    for link in links:
        if link.source == initialState.id and link.label == letter:
            stateId = link.target
    
    if stateId != -1:
        for node in nodes:
            if node.id == stateId:
                return node
    return stateId
            
    


# INICIO DE PROGRAMA
testFileName = sys.argv[1]
file = open(testFileName, "r")
content = file.read()

# tokens y keywords
tokens = []
keywords = []

# Nodos y Links de Tokens
nodes = []
links = []

# Nodos y Links de Keywords
keywordsNodes = []
keywordsLinks = []

lookahead = ''
lastToken = ''


# NODOS
nodes.append(Node('1', True, False))
nodes.append(Node('2', False, True))
nodes.append(Node('3', False, True))
nodes.append(Node('4', False, True))
nodes.append(Node('5', False, True))
nodes.append(Node('6', False, True))
nodes.append(Node('7', False, True))
nodes.append(Node('8', False, True))
nodes.append(Node('9', False, True))
nodes.append(Node('10', False, True))
nodes.append(Node('11', False, True))
nodes.append(Node('12', False, False))
nodes.append(Node('13', False, True))
nodes.append(Node('14', False, True))
nodes.append(Node('15', False, True))
nodes.append(Node('16', False, True))
nodes.append(Node('17', False, True))
nodes.append(Node('18', False, True))
nodes.append(Node('19', False, True))
nodes.append(Node('20', False, True))
nodes.append(Node('21', False, True))
nodes.append(Node('22', False, True))
nodes.append(Node('23', False, False))
nodes.append(Node('24', False, False))
nodes.append(Node('25', False, True))
nodes.append(Node('26', False, True))
nodes.append(Node('27', False, True))
nodes.append(Node('28', False, True))
nodes.append(Node('29', False, True))
nodes.append(Node('30', False, True))
nodes.append(Node('31', False, True))
nodes.append(Node('32', False, True))
nodes.append(Node('33', False, True))
nodes.append(Node('34', False, True))
nodes.append(Node('35', False, False))
nodes.append(Node('36', False, True))
nodes.append(Node('37', False, True))
nodes.append(Node('38', False, True))
nodes.append(Node('39', False, True))
nodes.append(Node('40', False, True))
nodes.append(Node('41', False, True))
nodes.append(Node('42', False, True))
nodes.append(Node('43', False, True))
nodes.append(Node('44', False, True))
nodes.append(Node('45', False, True))
nodes.append(Node('46', False, True))
nodes.append(Node('47', False, False))
nodes.append(Node('48', False, False))
nodes.append(Node('49', False, False))
nodes.append(Node('50', False, True))

links.append(Link('1', '2', '0'))
links.append(Link('1', '3', '1'))
links.append(Link('1', '4', '2'))
links.append(Link('1', '5', '3'))
links.append(Link('1', '6', '4'))
links.append(Link('1', '7', '5'))
links.append(Link('1', '8', '6'))
links.append(Link('1', '9', '7'))
links.append(Link('1', '10', '8'))
links.append(Link('1', '11', '9'))
links.append(Link('1', '12', '\n'))
links.append(Link('2', '13', '0'))
links.append(Link('2', '14', '1'))
links.append(Link('2', '15', '2'))
links.append(Link('2', '16', '3'))
links.append(Link('2', '17', '4'))
links.append(Link('2', '18', '5'))
links.append(Link('2', '19', '6'))
links.append(Link('2', '20', '7'))
links.append(Link('2', '21', '8'))
links.append(Link('2', '22', '9'))
links.append(Link('2', '23', '.'))
links.append(Link('3', '13', '0'))
links.append(Link('3', '14', '1'))
links.append(Link('3', '15', '2'))
links.append(Link('3', '16', '3'))
links.append(Link('3', '17', '4'))
links.append(Link('3', '18', '5'))
links.append(Link('3', '19', '6'))
links.append(Link('3', '20', '7'))
links.append(Link('3', '21', '8'))
links.append(Link('3', '22', '9'))
links.append(Link('3', '23', '.'))
links.append(Link('4', '13', '0'))
links.append(Link('4', '14', '1'))
links.append(Link('4', '15', '2'))
links.append(Link('4', '16', '3'))
links.append(Link('4', '17', '4'))
links.append(Link('4', '18', '5'))
links.append(Link('4', '19', '6'))
links.append(Link('4', '20', '7'))
links.append(Link('4', '21', '8'))
links.append(Link('4', '22', '9'))
links.append(Link('4', '23', '.'))
links.append(Link('5', '13', '0'))
links.append(Link('5', '14', '1'))
links.append(Link('5', '15', '2'))
links.append(Link('5', '16', '3'))
links.append(Link('5', '17', '4'))
links.append(Link('5', '18', '5'))
links.append(Link('5', '19', '6'))
links.append(Link('5', '20', '7'))
links.append(Link('5', '21', '8'))
links.append(Link('5', '22', '9'))
links.append(Link('5', '23', '.'))
links.append(Link('6', '13', '0'))
links.append(Link('6', '14', '1'))
links.append(Link('6', '15', '2'))
links.append(Link('6', '16', '3'))
links.append(Link('6', '17', '4'))
links.append(Link('6', '18', '5'))
links.append(Link('6', '19', '6'))
links.append(Link('6', '20', '7'))
links.append(Link('6', '21', '8'))
links.append(Link('6', '22', '9'))
links.append(Link('6', '23', '.'))
links.append(Link('7', '13', '0'))
links.append(Link('7', '14', '1'))
links.append(Link('7', '15', '2'))
links.append(Link('7', '16', '3'))
links.append(Link('7', '17', '4'))
links.append(Link('7', '18', '5'))
links.append(Link('7', '19', '6'))
links.append(Link('7', '20', '7'))
links.append(Link('7', '21', '8'))
links.append(Link('7', '22', '9'))
links.append(Link('7', '23', '.'))
links.append(Link('8', '13', '0'))
links.append(Link('8', '14', '1'))
links.append(Link('8', '15', '2'))
links.append(Link('8', '16', '3'))
links.append(Link('8', '17', '4'))
links.append(Link('8', '18', '5'))
links.append(Link('8', '19', '6'))
links.append(Link('8', '20', '7'))
links.append(Link('8', '21', '8'))
links.append(Link('8', '22', '9'))
links.append(Link('8', '23', '.'))
links.append(Link('9', '13', '0'))
links.append(Link('9', '14', '1'))
links.append(Link('9', '15', '2'))
links.append(Link('9', '16', '3'))
links.append(Link('9', '17', '4'))
links.append(Link('9', '18', '5'))
links.append(Link('9', '19', '6'))
links.append(Link('9', '20', '7'))
links.append(Link('9', '21', '8'))
links.append(Link('9', '22', '9'))
links.append(Link('9', '23', '.'))
links.append(Link('10', '13', '0'))
links.append(Link('10', '14', '1'))
links.append(Link('10', '15', '2'))
links.append(Link('10', '16', '3'))
links.append(Link('10', '17', '4'))
links.append(Link('10', '18', '5'))
links.append(Link('10', '19', '6'))
links.append(Link('10', '20', '7'))
links.append(Link('10', '21', '8'))
links.append(Link('10', '22', '9'))
links.append(Link('10', '23', '.'))
links.append(Link('11', '13', '0'))
links.append(Link('11', '14', '1'))
links.append(Link('11', '15', '2'))
links.append(Link('11', '16', '3'))
links.append(Link('11', '17', '4'))
links.append(Link('11', '18', '5'))
links.append(Link('11', '19', '6'))
links.append(Link('11', '20', '7'))
links.append(Link('11', '21', '8'))
links.append(Link('11', '22', '9'))
links.append(Link('11', '23', '.'))
links.append(Link('12', '24', '\r'))
links.append(Link('13', '13', '0'))
links.append(Link('13', '14', '1'))
links.append(Link('13', '15', '2'))
links.append(Link('13', '16', '3'))
links.append(Link('13', '17', '4'))
links.append(Link('13', '18', '5'))
links.append(Link('13', '19', '6'))
links.append(Link('13', '20', '7'))
links.append(Link('13', '21', '8'))
links.append(Link('13', '22', '9'))
links.append(Link('13', '23', '.'))
links.append(Link('14', '13', '0'))
links.append(Link('14', '14', '1'))
links.append(Link('14', '15', '2'))
links.append(Link('14', '16', '3'))
links.append(Link('14', '17', '4'))
links.append(Link('14', '18', '5'))
links.append(Link('14', '19', '6'))
links.append(Link('14', '20', '7'))
links.append(Link('14', '21', '8'))
links.append(Link('14', '22', '9'))
links.append(Link('14', '23', '.'))
links.append(Link('15', '13', '0'))
links.append(Link('15', '14', '1'))
links.append(Link('15', '15', '2'))
links.append(Link('15', '16', '3'))
links.append(Link('15', '17', '4'))
links.append(Link('15', '18', '5'))
links.append(Link('15', '19', '6'))
links.append(Link('15', '20', '7'))
links.append(Link('15', '21', '8'))
links.append(Link('15', '22', '9'))
links.append(Link('15', '23', '.'))
links.append(Link('16', '13', '0'))
links.append(Link('16', '14', '1'))
links.append(Link('16', '15', '2'))
links.append(Link('16', '16', '3'))
links.append(Link('16', '17', '4'))
links.append(Link('16', '18', '5'))
links.append(Link('16', '19', '6'))
links.append(Link('16', '20', '7'))
links.append(Link('16', '21', '8'))
links.append(Link('16', '22', '9'))
links.append(Link('16', '23', '.'))
links.append(Link('17', '13', '0'))
links.append(Link('17', '14', '1'))
links.append(Link('17', '15', '2'))
links.append(Link('17', '16', '3'))
links.append(Link('17', '17', '4'))
links.append(Link('17', '18', '5'))
links.append(Link('17', '19', '6'))
links.append(Link('17', '20', '7'))
links.append(Link('17', '21', '8'))
links.append(Link('17', '22', '9'))
links.append(Link('17', '23', '.'))
links.append(Link('18', '13', '0'))
links.append(Link('18', '14', '1'))
links.append(Link('18', '15', '2'))
links.append(Link('18', '16', '3'))
links.append(Link('18', '17', '4'))
links.append(Link('18', '18', '5'))
links.append(Link('18', '19', '6'))
links.append(Link('18', '20', '7'))
links.append(Link('18', '21', '8'))
links.append(Link('18', '22', '9'))
links.append(Link('18', '23', '.'))
links.append(Link('19', '13', '0'))
links.append(Link('19', '14', '1'))
links.append(Link('19', '15', '2'))
links.append(Link('19', '16', '3'))
links.append(Link('19', '17', '4'))
links.append(Link('19', '18', '5'))
links.append(Link('19', '19', '6'))
links.append(Link('19', '20', '7'))
links.append(Link('19', '21', '8'))
links.append(Link('19', '22', '9'))
links.append(Link('19', '23', '.'))
links.append(Link('20', '13', '0'))
links.append(Link('20', '14', '1'))
links.append(Link('20', '15', '2'))
links.append(Link('20', '16', '3'))
links.append(Link('20', '17', '4'))
links.append(Link('20', '18', '5'))
links.append(Link('20', '19', '6'))
links.append(Link('20', '20', '7'))
links.append(Link('20', '21', '8'))
links.append(Link('20', '22', '9'))
links.append(Link('20', '23', '.'))
links.append(Link('21', '13', '0'))
links.append(Link('21', '14', '1'))
links.append(Link('21', '15', '2'))
links.append(Link('21', '16', '3'))
links.append(Link('21', '17', '4'))
links.append(Link('21', '18', '5'))
links.append(Link('21', '19', '6'))
links.append(Link('21', '20', '7'))
links.append(Link('21', '21', '8'))
links.append(Link('21', '22', '9'))
links.append(Link('21', '23', '.'))
links.append(Link('22', '13', '0'))
links.append(Link('22', '14', '1'))
links.append(Link('22', '15', '2'))
links.append(Link('22', '16', '3'))
links.append(Link('22', '17', '4'))
links.append(Link('22', '18', '5'))
links.append(Link('22', '19', '6'))
links.append(Link('22', '20', '7'))
links.append(Link('22', '21', '8'))
links.append(Link('22', '22', '9'))
links.append(Link('22', '23', '.'))
links.append(Link('23', '25', '0'))
links.append(Link('23', '26', '1'))
links.append(Link('23', '27', '2'))
links.append(Link('23', '28', '3'))
links.append(Link('23', '29', '4'))
links.append(Link('23', '30', '5'))
links.append(Link('23', '31', '6'))
links.append(Link('23', '32', '7'))
links.append(Link('23', '33', '8'))
links.append(Link('23', '34', '9'))
links.append(Link('24', '35', '	'))
links.append(Link('25', '36', '0'))
links.append(Link('25', '37', '1'))
links.append(Link('25', '38', '2'))
links.append(Link('25', '39', '3'))
links.append(Link('25', '40', '4'))
links.append(Link('25', '41', '5'))
links.append(Link('25', '42', '6'))
links.append(Link('25', '43', '7'))
links.append(Link('25', '44', '8'))
links.append(Link('25', '45', '9'))
links.append(Link('26', '36', '0'))
links.append(Link('26', '37', '1'))
links.append(Link('26', '38', '2'))
links.append(Link('26', '39', '3'))
links.append(Link('26', '40', '4'))
links.append(Link('26', '41', '5'))
links.append(Link('26', '42', '6'))
links.append(Link('26', '43', '7'))
links.append(Link('26', '44', '8'))
links.append(Link('26', '45', '9'))
links.append(Link('27', '36', '0'))
links.append(Link('27', '37', '1'))
links.append(Link('27', '38', '2'))
links.append(Link('27', '39', '3'))
links.append(Link('27', '40', '4'))
links.append(Link('27', '41', '5'))
links.append(Link('27', '42', '6'))
links.append(Link('27', '43', '7'))
links.append(Link('27', '44', '8'))
links.append(Link('27', '45', '9'))
links.append(Link('28', '36', '0'))
links.append(Link('28', '37', '1'))
links.append(Link('28', '38', '2'))
links.append(Link('28', '39', '3'))
links.append(Link('28', '40', '4'))
links.append(Link('28', '41', '5'))
links.append(Link('28', '42', '6'))
links.append(Link('28', '43', '7'))
links.append(Link('28', '44', '8'))
links.append(Link('28', '45', '9'))
links.append(Link('29', '36', '0'))
links.append(Link('29', '37', '1'))
links.append(Link('29', '38', '2'))
links.append(Link('29', '39', '3'))
links.append(Link('29', '40', '4'))
links.append(Link('29', '41', '5'))
links.append(Link('29', '42', '6'))
links.append(Link('29', '43', '7'))
links.append(Link('29', '44', '8'))
links.append(Link('29', '45', '9'))
links.append(Link('30', '36', '0'))
links.append(Link('30', '37', '1'))
links.append(Link('30', '38', '2'))
links.append(Link('30', '39', '3'))
links.append(Link('30', '40', '4'))
links.append(Link('30', '41', '5'))
links.append(Link('30', '42', '6'))
links.append(Link('30', '43', '7'))
links.append(Link('30', '44', '8'))
links.append(Link('30', '45', '9'))
links.append(Link('31', '36', '0'))
links.append(Link('31', '37', '1'))
links.append(Link('31', '38', '2'))
links.append(Link('31', '39', '3'))
links.append(Link('31', '40', '4'))
links.append(Link('31', '41', '5'))
links.append(Link('31', '42', '6'))
links.append(Link('31', '43', '7'))
links.append(Link('31', '44', '8'))
links.append(Link('31', '45', '9'))
links.append(Link('32', '36', '0'))
links.append(Link('32', '37', '1'))
links.append(Link('32', '38', '2'))
links.append(Link('32', '39', '3'))
links.append(Link('32', '40', '4'))
links.append(Link('32', '41', '5'))
links.append(Link('32', '42', '6'))
links.append(Link('32', '43', '7'))
links.append(Link('32', '44', '8'))
links.append(Link('32', '45', '9'))
links.append(Link('33', '36', '0'))
links.append(Link('33', '37', '1'))
links.append(Link('33', '38', '2'))
links.append(Link('33', '39', '3'))
links.append(Link('33', '40', '4'))
links.append(Link('33', '41', '5'))
links.append(Link('33', '42', '6'))
links.append(Link('33', '43', '7'))
links.append(Link('33', '44', '8'))
links.append(Link('33', '45', '9'))
links.append(Link('34', '36', '0'))
links.append(Link('34', '37', '1'))
links.append(Link('34', '38', '2'))
links.append(Link('34', '39', '3'))
links.append(Link('34', '40', '4'))
links.append(Link('34', '41', '5'))
links.append(Link('34', '42', '6'))
links.append(Link('34', '43', '7'))
links.append(Link('34', '44', '8'))
links.append(Link('34', '45', '9'))
links.append(Link('35', '46', ' '))
links.append(Link('36', '36', '0'))
links.append(Link('36', '37', '1'))
links.append(Link('36', '38', '2'))
links.append(Link('36', '39', '3'))
links.append(Link('36', '40', '4'))
links.append(Link('36', '41', '5'))
links.append(Link('36', '42', '6'))
links.append(Link('36', '43', '7'))
links.append(Link('36', '44', '8'))
links.append(Link('36', '45', '9'))
links.append(Link('37', '36', '0'))
links.append(Link('37', '37', '1'))
links.append(Link('37', '38', '2'))
links.append(Link('37', '39', '3'))
links.append(Link('37', '40', '4'))
links.append(Link('37', '41', '5'))
links.append(Link('37', '42', '6'))
links.append(Link('37', '43', '7'))
links.append(Link('37', '44', '8'))
links.append(Link('37', '45', '9'))
links.append(Link('38', '36', '0'))
links.append(Link('38', '37', '1'))
links.append(Link('38', '38', '2'))
links.append(Link('38', '39', '3'))
links.append(Link('38', '40', '4'))
links.append(Link('38', '41', '5'))
links.append(Link('38', '42', '6'))
links.append(Link('38', '43', '7'))
links.append(Link('38', '44', '8'))
links.append(Link('38', '45', '9'))
links.append(Link('39', '36', '0'))
links.append(Link('39', '37', '1'))
links.append(Link('39', '38', '2'))
links.append(Link('39', '39', '3'))
links.append(Link('39', '40', '4'))
links.append(Link('39', '41', '5'))
links.append(Link('39', '42', '6'))
links.append(Link('39', '43', '7'))
links.append(Link('39', '44', '8'))
links.append(Link('39', '45', '9'))
links.append(Link('40', '36', '0'))
links.append(Link('40', '37', '1'))
links.append(Link('40', '38', '2'))
links.append(Link('40', '39', '3'))
links.append(Link('40', '40', '4'))
links.append(Link('40', '41', '5'))
links.append(Link('40', '42', '6'))
links.append(Link('40', '43', '7'))
links.append(Link('40', '44', '8'))
links.append(Link('40', '45', '9'))
links.append(Link('41', '36', '0'))
links.append(Link('41', '37', '1'))
links.append(Link('41', '38', '2'))
links.append(Link('41', '39', '3'))
links.append(Link('41', '40', '4'))
links.append(Link('41', '41', '5'))
links.append(Link('41', '42', '6'))
links.append(Link('41', '43', '7'))
links.append(Link('41', '44', '8'))
links.append(Link('41', '45', '9'))
links.append(Link('42', '36', '0'))
links.append(Link('42', '37', '1'))
links.append(Link('42', '38', '2'))
links.append(Link('42', '39', '3'))
links.append(Link('42', '40', '4'))
links.append(Link('42', '41', '5'))
links.append(Link('42', '42', '6'))
links.append(Link('42', '43', '7'))
links.append(Link('42', '44', '8'))
links.append(Link('42', '45', '9'))
links.append(Link('43', '36', '0'))
links.append(Link('43', '37', '1'))
links.append(Link('43', '38', '2'))
links.append(Link('43', '39', '3'))
links.append(Link('43', '40', '4'))
links.append(Link('43', '41', '5'))
links.append(Link('43', '42', '6'))
links.append(Link('43', '43', '7'))
links.append(Link('43', '44', '8'))
links.append(Link('43', '45', '9'))
links.append(Link('44', '36', '0'))
links.append(Link('44', '37', '1'))
links.append(Link('44', '38', '2'))
links.append(Link('44', '39', '3'))
links.append(Link('44', '40', '4'))
links.append(Link('44', '41', '5'))
links.append(Link('44', '42', '6'))
links.append(Link('44', '43', '7'))
links.append(Link('44', '44', '8'))
links.append(Link('44', '45', '9'))
links.append(Link('45', '36', '0'))
links.append(Link('45', '37', '1'))
links.append(Link('45', '38', '2'))
links.append(Link('45', '39', '3'))
links.append(Link('45', '40', '4'))
links.append(Link('45', '41', '5'))
links.append(Link('45', '42', '6'))
links.append(Link('45', '43', '7'))
links.append(Link('45', '44', '8'))
links.append(Link('45', '45', '9'))
links.append(Link('46', '47', '\n'))
links.append(Link('47', '48', '\r'))
links.append(Link('48', '49', '	'))
links.append(Link('49', '50', ' '))
links.append(Link('50', '47', '\n'))

keywordsNodes.append(Node('1', True, False))
keywordsNodes.append(Node('2', False, False))
keywordsNodes.append(Node('3', False, False))
keywordsNodes.append(Node('4', False, False))
keywordsNodes.append(Node('5', False, True))
keywordsNodes.append(Node('6', False, False))
keywordsNodes.append(Node('7', False, False))
keywordsNodes.append(Node('8', False, True))

keywordsLinks.append(Link('1', '2', 'w'))
keywordsLinks.append(Link('1', '3', 'd'))
keywordsLinks.append(Link('2', '4', 'h'))
keywordsLinks.append(Link('3', '5', 'o'))
keywordsLinks.append(Link('4', '6', 'i'))
keywordsLinks.append(Link('6', '7', 'l'))
keywordsLinks.append(Link('7', '8', 'e'))

def Stat():
    value=0
    value=Expression()
    print("Resultado:" + value)

def Expression():
    result1=0,result2=0
    result1=Term()
    while lookahead=="+" or lookahead=="-":
        if lookahead=="+":
            result2=Term()
            result1+=result2
        elif lookahead=='-':
            result2=Term()
            result1-=result2
    return result1

def Term():
    result1=0,result2=0
    result1=Factor()
    while lookahead=="*" or lookahead=="/":
        if lookahead=="*":
            result2=Factor()
            result1*=result2
        elif lookahead=="/":
            result2=Factor()
            result1/=result2
    return result1

def Factor():
    sign=1
    if lookahead=="-":
        sign=-1
    if lookahead=="(":
        result=Expression()
    else:
        result=Number()
    return result*sign

def Number():
    if isNumber(lookahead):
        result = float(lastToken)
    elif isDecNumber(lookahead):
        result = float(lastToken)