import decision_arbol


def main():
    # Insert input file

    file = open('datos_2.csv')

    target = "class"
    data = [[]]
    for line in file:
        line = line.strip("\r\n")
        data.append(line.split(','))
    data.remove([])
    attributes = data[0]
    data.remove(attributes)
    # Run ID3
    tree = decision_arbol.makeTree(data, attributes, target, 0)
    print
    "genera decision el arbol"
    # Generate program
    file = open('programa_arbol.py', 'w')
    file.write("import nodo\n\n")
    # open input file
    file.write("data = [[]]\n")
    """
    cambios en el path del data del archivo
    """
    file.write("f = open('dato.csv')\n")

    file.write("for line in f:\n\tline = line.strip(\"\\r\\n\")\n\tdata.append(line.split(','))\n")
    file.write("data.remove([])\n")

    file.write("tree = %s\n" % str(tree))
    file.write("attributes = %s\n" % str(attributes))
    file.write("count = 0\n")
    file.write("for entry in data:\n")
    file.write("\tcount += 1\n")

    file.write("\ttempDict = tree.copy()\n")
    file.write("\tresult = \"\"\n")

    file.write("\twhile(isinstance(tempDict, dict)):\n")
    file.write("\t\troot = Node.Node(tempDict.keys()[0], tempDict[tempDict.keys()[0]])\n")
    file.write("\t\ttempDict = tempDict[tempDict.keys()[0]]\n")
    # this must be attribute
    file.write("\t\tindex = attributes.index(root.value)\n")
    file.write("\t\tvalue = entry[index]\n")
    # ensure that key exists
    file.write("\t\tif(value in tempDict.keys()):\n")
    file.write("\t\t\tchild = Node.Node(value, tempDict[value])\n")
    file.write("\t\t\tresult = tempDict[value]\n")
    file.write("\t\t\ttempDict = tempDict[value]\n")
    # otherwise, break
    file.write("\t\telse:\n")
    file.write("\t\t\tprint \"can't process input %s\" % count\n")
    file.write("\t\t\tresult = \"?\"\n")
    file.write("\t\t\tbreak\n")
    # print solutions
    file.write("\tprint (\"entry%s = %s\" % (count, result))\n")



if __name__ == '__main__':
    main()