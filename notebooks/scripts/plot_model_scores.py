import matplotlib.pyplot as plt
import numpy as np

def get_plot_model(model_names: list, f1_scores: list, recall_scores: list, precision_scores: list, title: str = None) -> plt.figure:
  """
  Creates a horizontal bar chart comparing evaluation scores (F1, Recall, Precision) for different models. 

  Parameters:
    model_names (list): List of model names
    f1_scores (list): List of F1 scores for the models
    recall_scores (list): List of recall scores for the models
    precision_scores (list): List of precision scores for the models
    
  Returns: 
    plt.figure: A pyplot figure
  """
  
  metrics = ['F1 Score', 'Recall', 'Precision']
  num_models = len(model_names)
  bar_width = 0.35 # Width of the bars
  index = np.arange(len(metrics))

  fig, ax = plt.subplots(figsize=(10, 6))

  for i, model_name in enumerate(model_names):
    bars = ax.barh(index + i * bar_width, [f1_scores[i], recall_scores[i], precision_scores[i]], bar_width,
                  label=model_name)
    for bar in bars:
      width = bar.get_width()
      ax.annotate(f'{width:.2f}', xy=(width, bar.get_y() + bar.get_height() / 2),
                  xytext=(3, 0), textcoords='offset points', ha='left', va='center')

  ax.set_xlabel('Scores')
  if title is None:
    ax.set_title('Model Comparison - F1, Recall, Precision')
  else: 
    ax.set_title(title)
  ax.set_yticks(index + bar_width * (num_models - 1) / 2)
  ax.set_yticklabels(metrics)
  ax.set_xlim(0, 1)  # Set the x-axis limit to [0, 1] for consistency with score range
  ax.legend(loc='lower right')

  # Display the chart
  return fig

def dummy():
  # We now evaluate our model performances on this dataset and compare against the Naive Bayes benchmark
  precision_naive_bayes = precision_score(y_true=y_test, y_pred=y_pred_naive_bayes)
  recall_naive_bayes = recall_score(y_true=y_test, y_pred=y_pred_naive_bayes)
  f1_naive_bayes = f1_score(y_test, y_pred_naive_bayes)

  precision_automl = precision_score(y_true=y_test, y_pred=y_pred_automl)
  recall_automl = recall_score(y_true=y_test, y_pred=y_pred_automl)
  f1_automl = f1_score(y_true=y_test, y_pred=y_pred_automl)

  model_names = ['Naive Bayes', 'AutoML-LinearSVC']
  f1_scores = [f1_naive_bayes, f1_automl]
  recall_scores = [recall_naive_bayes, recall_automl]
  precision_scores = [precision_naive_bayes, precision_automl]