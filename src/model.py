import numpy as np
import random
class MetaPathGenerator(object):
    def __init__(self):
        self.paper_author = dict ()
        self.author_paper = dict ()
        self.paper_org = dict ()
        self.org_paper = dict ()
        self.paper_conf = dict ()
        self.conf_paper = dict ()

    ##########read author's feature and write the paper's relation to files#######################
    def read_data (self, dirpath):
        temp = set ()
        with open (dirpath + "/paper_org.txt", encoding='utf-8') as pafile:
            for line in pafile:
                temp.add (line)
        for line in temp:
            toks = line.strip ().split ("\t")
            if len (toks) == 2:
                p, a = toks[0], toks[1]
                if p not in self.paper_org:
                    self.paper_org[p] = []
                self.paper_org[p].append (a)
                if a not in self.org_paper:
                    self.org_paper[a] = []
                self.org_paper[a].append (p)
        temp.clear ()

        with open (dirpath + "/paper_author.txt", encoding='utf-8') as pafile:
            for line in pafile:
                temp.add (line)
        for line in temp:
            toks = line.strip ().split ("\t")
            if len (toks) == 2:
                p, a = toks[0], toks[1]
                if p not in self.paper_author:
                    self.paper_author[p] = []
                self.paper_author[p].append (a)
                if a not in self.author_paper:
                    self.author_paper[a] = []
                self.author_paper[a].append (p)
        temp.clear ()

        with open (dirpath + "/paper_conf.txt", encoding='utf-8') as pcfile:
            for line in pcfile:
                temp.add (line)
        for line in temp:
            toks = line.strip ().split ("\t")
            if len (toks) == 2:
                p, a = toks[0], toks[1]
                if p not in self.paper_conf:
                    self.paper_conf[p] = []
                self.paper_conf[p].append (a)
                if a not in self.conf_paper:
                    self.conf_paper[a] = []
                self.conf_paper[a].append (p)
        temp.clear ()

        # print ("#papers ", len (self.paper_conf))
        # print ("#authors", len (self.author_paper))
        # print ("#org_words", len (self.org_paper))
        # print ("#confs  ", len (self.conf_paper))

    ######generate the random walk's meta path##############
    def generate_WMRW (self, outfilename, numwalks, walklength):
        outfile = open (outfilename, 'w')
        for paper0 in self.paper_conf:
            for j in range (0, numwalks):  # wnum walks
                paper = paper0
                outline = ""
                i = 0
                while (i < walklength):
                    i = i + 1
                    if paper in self.paper_author:
                        authors = self.paper_author[paper]
                        numa = len (authors)
                        authorid = random.randrange (numa)
                        author = authors[authorid]

                        papers = self.author_paper[author]
                        nump = len (papers)
                        if nump > 1:
                            paperid = random.randrange (nump)
                            paper1 = papers[paperid]
                            while paper1 == paper:
                                paperid = random.randrange (nump)
                                paper1 = papers[paperid]
                            paper = paper1
                            outline += " " + paper

                    if paper in self.paper_org:
                        words = self.paper_org[paper]
                        numw = len (words)
                        wordid = random.randrange (numw)
                        word = words[wordid]

                        papers = self.org_paper[word]
                        nump = len (papers)
                        if nump > 1:
                            paperid = random.randrange (nump)
                            paper1 = papers[paperid]
                            while paper1 == paper:
                                paperid = random.randrange (nump)
                                paper1 = papers[paperid]
                            paper = paper1
                            outline += " " + paper

                outfile.write (outline + "\n")
        outfile.close ()