from dis import dis
from matplotlib import pyplot as plt
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve, auc
from IPython.display import display, Markdown
import pandas as pd

COLOR_VINO_TINTO = "#7C3030"

BASIC_METRICS = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']

def calculate_metrics(algorithm_name,algorithm,x_test, y_test, y_test_pred):
    """Calcula las metricas de precision, recall, f1, accuracy, y roc"""
    accuracy = accuracy_score(y_test, y_test_pred)
    precision = precision_score(y_test, y_test_pred)
    recall = recall_score(y_test, y_test_pred)
    f1 = f1_score(y_test, y_test_pred)
    roc_auc = calculate_roc_auc(algorithm, x_test, y_test)
    metrics = {'accuracy': accuracy, 'precision': precision, 'recall': recall, 'f1': f1,'roc_auc': roc_auc["roc_auc"]}
    roc_auc_plot = {'fpr': roc_auc['fpr'], 'tpr': roc_auc['tpr'], 'thresholds': roc_auc['thresholds']}
    df_metrics = pd.DataFrame.from_dict(metrics, orient='index',columns=[algorithm_name]).round(2)
    df_roc_auc_plot = pd.DataFrame(pd.Series(roc_auc_plot),columns=[algorithm_name])
    return pd.concat([df_metrics, df_roc_auc_plot], axis=0)

def calculate_roc_auc(algorithm, x_test, y_test):
    """Calcula el area bajo la curva roc"""
    class_probabilities = algorithm.predict_proba(x_test)
    preds = class_probabilities[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, preds)
    roc_auc = auc(fpr, tpr)
    return {'fpr': fpr, 'tpr': tpr, 'thresholds': thresholds, 'roc_auc': roc_auc}


def display_calculated_metrics(algorithm_name,algorithm, x_test, y_test, y_test_pred):
    display(Markdown('### Metricas calculadas'))
    metrics = calculate_metrics(algorithm_name,algorithm, x_test, y_test, y_test_pred).T[BASIC_METRICS].T.sort_values(by=algorithm_name, ascending=False).T
    display(metrics)
    metrics.T.plot(kind='bar', color=COLOR_VINO_TINTO)

def display_confusion_matrix(algorithm, y_test, y_test_pred):
    """Muestra la confusion matrix"""
    display(Markdown('### Grafico de confusion matrix: '))
    plt.figure(figsize=(10, 10))
    cm = confusion_matrix(y_test, y_test_pred, labels=algorithm.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=algorithm.classes_)
    disp.plot()
    plt.show()
    plt.close()

def plot_roc_curve(algorithm, x_test, y_test):
    """Muestra la curva roc"""
    metrics = calculate_roc_auc(algorithm, x_test, y_test)
    display(Markdown('### Grafico de roc: '))
    plt.plot(metrics['fpr'], metrics['tpr'],'b', label='ROC curve (area = %0.2f)' % metrics['roc_auc'])
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc="lower right")
    plt.show()
    plt.close()


def display_and_plot_all_metrics(algorithm_name,algorithm, x_test, y_test, y_test_pred):
    display(Markdown('# Metricas: '))
    display_calculated_metrics(algorithm_name,algorithm, x_test, y_test, y_test_pred)
    display_confusion_matrix(algorithm, y_test, y_test_pred)
    plot_roc_curve(algorithm, x_test, y_test)