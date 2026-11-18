# cnn-ml-class
CNN Color Inference Project for Machine Learning class
TODO:
1. Find a dataset to work with.  Make sure the dataset is colored images.  Make a note on what type of dataset it is (i.e. if the dataset is describing people or cats or dogs, if the dataset has uniform resolution in its images, how large the dataset is)
2. Write a display function which prints some relevant statistics about the data and some example data points 
3. Write a preprocess function which checks and modifies the input to some standard we choose.
4. Write a toGreyscale function which converts colored images to greyscale (just set all color channels to their average for each pixel).
5. Establish a cnn (i think its on sklearn)  (do some research on cnn's hyperparameters and what to set it to)
5a. Write a function that determines hyperparameters automatically.
6. Write a function (or use sklearn) to split the dataset into training, testing, and validation.
7. Write a function that plots our results with any important metrics

examplemain() {
    d=importDataFrom(somewhere)
    displayFacts(d)

    d=clean(d)  //if necessary      //targets


    train, test, validation = split(d)
    train_grey, test_grey, validation_grey = toGreyscale(train.copy(), test.copy(), validation.copy())

    cnn.setHyperparameters(validation_grey, validation)

    model = cnn.fit(train_grey, train)

    predictions = model.predict(test_grey);
    
    displayResults(predictions, test_grey, hyperparameters, etcetera)


}