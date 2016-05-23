from graphviz import Digraph
dot = Digraph(name = 'Amazon')

the = 300
max_weight = 0.0
node = []
node_weight = []

#init node weight
for i in range(the):
    node.append(0)
    node_weight.append(0)

#set graph


#get node weight
with open('Amazon0302 copy.txt', "r+") as f:
    for s in f:
        s = s.rstrip('\r\n')
        s = s.split('\t')
        if (int(s[0]) < the and int(s[1]) < the):
            node[int(s[1])] += 1
            node_weight[int(s[1])] += 1
            if (node[int(s[1])] > max_weight):
                max_weight = node[int(s[1])]

#set node
for i in range(the):
    dot.attr('node', fontsize = str(20 + float(node[i]) / max_weight * 100))
    if (float(node[i]) / max_weight > 0.8):
        dot.attr('node', color = 'red',  style = 'filled')
    elif (float(node[i]) / max_weight > 0.6):
        dot.attr('node', color = 'red1', style = 'filled')
    elif (float(node[i]) / max_weight > 0.4):
        dot.attr('node', color = 'red2', style = 'filled')
    elif (float(node[i]) / max_weight > 0.2):
        dot.attr('node', color = 'red3', style = 'filled')
    else:
        dot.attr('node', color = 'red4', style='filled')
    dot.node(str(i), 'Item: ' + str(i) + '\nClick:' + str(node[i]))

#set edge
with open('Amazon0302 copy.txt', "r+") as f:
    for s in f:
        s = s.rstrip('\r\n')
        s = s.split('\t')
        if (int(s[0]) < the and int(s[1]) < the):
            if (float(node[int(s[1])]) / max_weight > 0.8):
                dot.attr('edge', penwidth = '5')
                dot.attr('edge', arrowsize = '5')
            elif (float(node[int(s[1])]) / max_weight > 0.6):
                dot.attr('edge', penwidth = '4')
                dot.attr('edge', arrowsize = '4')
            elif (float(node[int(s[1])]) / max_weight > 0.4):
                dot.attr('edge', penwidth = '3')
                dot.attr('edge', arrowsize = '3')
            elif (float(node[int(s[1])]) / max_weight > 0.2):
                dot.attr('edge', penwidth = '2')
                dot.attr('edge', arrowsize = '2')
            else:
                dot.attr('edge', penwidth = '1')
                dot.attr('edge', arrowsize = '1')
            dot.edge(str(s[0]), str(s[1]))

#print(dot.source)
dot.body.append(r'label = "\n\nAmazon Popular Item (' + str(the) +' items)\ndrawn by Yuan-Fu Lou"')
dot.body.append('fontsize = 100')
dot.render('test-output/amazon.gv', view=True)
