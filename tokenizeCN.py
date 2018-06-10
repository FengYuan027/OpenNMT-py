import nltk

InputFile = "/Users/yuanfeng/ComputerScience/AI/C-E datasetcopy/trainCN.txt"
OutputFile = "/Users/yuanfeng/ComputerScience/AI/C-E datasetcopy/trainCN_tokenized.txt"

lines = list(open(InputFile))

with open(OutputFile, "w") as f:
    f.write(
        "".join([
            " ".join([c if c != " " else "<s>" for c in l])
            for l in lines
        ])
    )