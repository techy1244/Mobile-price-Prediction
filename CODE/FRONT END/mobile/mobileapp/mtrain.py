import pandas as pd
from . import data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import StackingClassifier
from sklearn.metrics import accuracy_score,classification_report



class Train:
    def prepro():
        global x_train,x_test,y_train,y_test
        df = data.readD()
        x=df.drop('price_range',axis=1)
        y=df['price_range']
        # splitting the data into training and testing part
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)
    
    prepro()
    
    def rf_train():
        # Initialize and train the Random Forest model
        rfc = RandomForestClassifier(random_state=42)
        rfc.fit(x_train, y_train)
        y_pred_rfc = rfc.predict(x_test)
        # Calculate evaluation metrics for Random Forest
        acc_rfc = accuracy_score(y_test, y_pred_rfc) * 100

        report_rfc = classification_report(y_test, y_pred_rfc)
        # Calculate time taken for training and prediction
        return report_rfc

    def lr_train():
        le = LogisticRegression()
        le.fit(x_train,y_train)
        le_pred = le.predict(x_test)
        le_acc = accuracy_score(le_pred,y_test)
        cl_le = classification_report(le_pred,y_test)
        return cl_le
    
    def hy_train():
        global stacking_classifier
        # Initialize base models
        base_models = [
            ('logistic_regression', LogisticRegression()),
            ('random_forest', RandomForestClassifier(random_state=42))
        ]
        # Initialize the stacking classifier
        stacking_classifier = StackingClassifier(estimators=base_models, final_estimator=LogisticRegression())
        # Fit the stacking classifier on the training data
        stacking_classifier.fit(x_train, y_train)
        # Predict with the stacking classifier
        stacked_predictions = stacking_classifier.predict(x_test)
        # Calculate accuracy
        stacked_accuracy = accuracy_score(y_test, stacked_predictions)
        # Generate classification report
        stacked_report = classification_report(y_test, stacked_predictions)
        return stacked_report
    
    def hy_trai():
        global stacking_classifier
        # Initialize base models
        base_models = [
            ('logistic_regression', LogisticRegression()),
            ('random_forest', RandomForestClassifier(random_state=42))
        ]
        # Initialize the stacking classifier
        stacking_classifier = StackingClassifier(estimators=base_models, final_estimator=LogisticRegression())
        # Fit the stacking classifier on the training data
        stacking_classifier.fit(x_train, y_train)
        return stacking_classifier
    
    
    def x_trr():
        global x_train,x_test,y_train,y_test
        df = data.readD()
        x=df.drop('price_range',axis=1)
        y=df['price_range']
        # splitting the data into training and testing part
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)
        return x_train