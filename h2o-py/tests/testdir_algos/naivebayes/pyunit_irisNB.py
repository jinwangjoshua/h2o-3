



def nb_iris():
    

    print "Importing iris_wheader.csv data...\n"
    iris = h2o.upload_file(pyunit_utils.locate("smalldata/iris/iris_wheader.csv"))
    iris.describe()

    laplace_range = [0, 1, 0.25]
    for i in laplace_range:
        print "H2O Naive Bayes with Laplace smoothing = {0}".format(i)
        iris_nbayes = h2o.naive_bayes(x=iris[0:4], y=iris[4], laplace=i)
        iris_nbayes.show()


nb_iris()
