func examplemain {
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