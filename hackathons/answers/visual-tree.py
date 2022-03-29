from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(20,24))
plot_tree(pipeline_fewer_features['model'], 
          ax=ax,
          feature_names = new_features, 
          fontsize=10,
         filled=True);