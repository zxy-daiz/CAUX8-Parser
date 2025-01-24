import xml.etree.ElementTree as ET

from moodle.coderunner.question import qtype_coderunner_question

with open("../coderunner/builtin_PROTOTYPES.xml","r") as f:
    tree = ET.parse(f)
    f.close()

proto = []

for question in tree.findall("question"):
    if question.get("type") == "coderunner":
        q = qtype_coderunner_question()
        attr = vars(q)
        for node in question.findall("*"):
            if node.tag in attr:
                del attr[node.tag]
            else:
                print(node.tag + " not in attr.")
        for item in attr:
            print(item + " not matched.")
        proto.append(q)
        break

print(proto)