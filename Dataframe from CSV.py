def getDFFromCSV(filename):
    if os.path.isfile(filename):
        return pandas.read_csv(filename)
    else:
        raise IOError
