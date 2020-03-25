#!/usr/bin/env python

import os
import sys

CAT_NAME = "sandbox"
INDEX_TEMP = "./_index.rst"

def generateIndex(inDir, outDir, listModules):
    # listModules = []
    # for fileName in os.listdir(inDir) :
    #     print(fileName)
    #     if os.path.isdir(inDir + fileName):
    #         listModules.append(fileName)  
    # listModules = sorted(listModules)

    # generate index.rst
    with open(INDEX_TEMP, "r") as inFile:
        with open(outDir + "/index.rst", "w") as outFile:
            for line in inFile :
                outFile.write(line)
            # outFile.write("   :caption: %s:\n\n" % CAT_NAME)
            for moduleName in listModules :
                outFile.write("   {moduleName}/{moduleName}\n".format(moduleName = moduleName))

def generateFile(outDir, moduleName, shortName, listFiles):
    print('****\noutDir = {}\nmoduleName = {}\nshortName = {}\nlistFiles = {}'.format(
        outDir, moduleName, shortName, listFiles))

    if not os.path.isdir(outDir):
        os.mkdir(outDir)

    print('**** {}'.format(outDir))

    # title
    with open('{}/{}.rst'.format(outDir, shortName), "w") as outFile:
        outFile.write(shortName[0].upper() + shortName[1:] + "\n")
        outFile.write("=" * len(shortName) + "\n\n")

        doxyfile_rel_path = outDir

        if doxyfile_rel_path.startswith('../'):
            doxyfile_rel_path = doxyfile_rel_path[3:]
        elif doxyfile_rel_path.startswith('./'):
            doxyfile_rel_path = doxyfile_rel_path[2:]

        print('####', doxyfile_rel_path)
        print(".. doxygenfile:: {}/{}\n".format(doxyfile_rel_path, shortName))

        # doxygenfile
        for fileName in listFiles:
            outFile.write(".. doxygenfile:: {}/{}\n".format(doxyfile_rel_path, fileName))

        # toctree
        outFile.write(".. toctree::\n")

def generateRST(outDir, moduleName, listModules, listFiles) :
    print('****\noutDir = {}\nmoduleName = {}\nlistModules = {}\nlistFiles = {}'.format(
        outDir, moduleName, listModules, listFiles))

    if not os.path.isdir(outDir):
        os.mkdir(outDir)

    print('**** {}'.format(outDir))

    subFiles={}
    for fileName in listFiles:
        if fileName.rfind('.') >= 0:
            shortName = fileName[:fileName.rfind('.')]
        else:
            shortName = fileName

        if shortName not in subFiles:
            subFiles[shortName] = []
        
        subFiles[shortName].append(fileName)

    # doxygenfile
    for shortName, files in subFiles.items() :
        generateFile(outDir, moduleName, shortName, files)

    # title
    with open('{}/{}.rst'.format(outDir, moduleName), "w") as outFile:
        outFile.write(moduleName[0].upper() + moduleName[1:] + "\n")
        outFile.write("=" * len(moduleName) + "\n\n")

        # doxygenfile
        # for fileName in subFiles :
        #     outFile.write(".. doxygenfile:: %s/%s\n" % (outDir[3:], fileName))
        #     outFile.write("   :project: sandbox\n\n")

        # outFile.write(".. doxygenindex::\n")
        # outFile.write(".. doxygenfunction::\n")
        # outFile.write(".. doxygenstruct::\n")
        # outFile.write(".. doxygenenum::\n")
        # outFile.write(".. doxygentypedef::\n")
        # outFile.write(".. doxygenclass::\n")

        # toctree
        outFile.write(".. toctree::\n")
        # outFile.write("   :caption: %s:\n" % CAT_NAME)
        # outFile.write("   :titlesonly:\n")
        # outFile.write("   :maxdepth: 50\n")
        # outFile.write("   :hidden:\n\n")

        for childModuleName in listModules :
            outFile.write("   {}/{}\n" % (moduleName, childModuleName) )

        for shortName, files in subFiles.items() :
            outFile.write("   {}\n".format(shortName))

def generateRSTs(inDir, outDir, isRoot=False):
    listModules = []
    listFiles = []
    for fileName in os.listdir(inDir) :
        if os.path.isdir(inDir + "/" + fileName):
            listModules.append(fileName)  
        else :
            fileExt = fileName.split(".")[-1]
            if fileExt == "hpp" or fileExt == "cpp" :
                listFiles.append(fileName)
    
    listModules = sorted(listModules)
    listFiles = sorted(listFiles)

    print('*******\nisRoot = {}\ninDir = {}\noutDir = {}\nlistModules = {}\nlistFiles = {}'.format(
        isRoot, inDir, outDir, ', '.join(listModules), ', '.join(listFiles)))

    if not isRoot :
        moduleName = outDir.split("/")[-1]
        generateRST(outDir, moduleName, listModules, listFiles)

    for moduleName in listModules :
        curInDir = inDir + "/" + moduleName
        curOutDir = outDir + "/" + moduleName

        generateRSTs(curInDir, curOutDir, False)
    
    return listModules

'''
Alphabet
========
.. doxygenfile:: alphabet.hpp
   :project: myproject
.. doxygenfile:: alphabet_container.hpp
   :project: myproject
.. doxygenfile:: compound_alphabet.hpp
   :project: myproject
.. toctree::
   :caption: sandbox:
   alphabet/aminoacid
   alphabet/gaps
   alphabet/nucleotide
'''


#    print(listModules)
#    print(listFiles)


###################
inDir = sys.argv[1]
outDir = sys.argv[2]

listModules = generateRSTs(inDir, outDir, True)
generateIndex(inDir, outDir, listModules)

