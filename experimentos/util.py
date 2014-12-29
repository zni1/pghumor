# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

from sklearn import metrics


def entrenar_y_evaluar(clasificador, X_train, X_test, y_train, y_test):
    clasificador.fit(X_train, y_train)

    print("Acierto en el conjunto de entrenamiento: ", str(clasificador.score(X_train, y_train)))
    print("Acierto en el conjunto de evaluación: ", str(clasificador.score(X_test, y_test)))

    y_pred = clasificador.predict(X_test)

    print("Reporte de clasificación:")
    print(metrics.classification_report(y_test, y_pred))
    print("Matriz de confusión:")
    print(metrics.confusion_matrix(y_test, y_pred))
