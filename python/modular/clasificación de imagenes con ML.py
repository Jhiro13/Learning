from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
mnist=fetch_openml('mnist_784', as_frame=False)#ára descargar conjuntos de datos
x,y=mnist["data"], mnist["target"]
#VISUALIZANDO (para uno y para varios)
"""some_digit=x[0]
some_digit_image=some_digit.reshape(28,28)
plt.imshow(some_digit_image, cmap='gray')
plt.axis('off')  # Ocultar los ejes
plt.show()"""
def plot_digits(instances, images_per_row=10):
    size = 28  # Tamaño de cada imagen
    images = [instance.reshape(size, size) for instance in instances]
    n_rows = (len(images) // images_per_row) + 1

    plt.figure(figsize=(images_per_row, n_rows))
    for index, image in enumerate(images):
        plt.subplot(n_rows, images_per_row, index + 1)
        plt.imshow(image, cmap='gray', interpolation='nearest')
        plt.axis('off')
    plt.show()

plot_digits(x[:20])  # Muestra las primeras 20 imágenes
#Dividir en subconjuntos de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)#random_state es la semilla, la puedes borrar si quieres
# Crear el clasificador
clf = RandomForestClassifier(n_estimators=100, random_state=42)#random_state es la semilla, la puedes borrar si quieres

# Entrenar el modelo
clf.fit(X_train, y_train)
# Hacer predicciones
y_pred = clf.predict(X_test)
# Calcular la precisión
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

# Mostrar la matriz de confusión
cm = confusion_matrix(y_test, y_pred)
print('Matriz de confusión:')
print(cm)
# Identificar las imágenes clasificadas incorrectamente
incorrect_indices = np.where(y_pred != y_test)[0]
incorrect_images = X_test[incorrect_indices]
incorrect_labels = y_test[incorrect_indices]
predicted_labels = y_pred[incorrect_indices]

# Visualizar algunas imágenes clasificadas incorrectamente
def plot_incorrect_predictions(images, true_labels, predicted_labels, images_per_row=5):
    size = 28  # Tamaño de cada imagen
    n_rows = (len(images) // images_per_row) + 1

    plt.figure(figsize=(images_per_row * 2, n_rows * 2))
    for index in range(len(images)):
        plt.subplot(n_rows, images_per_row, index + 1)
        plt.imshow(images[index].reshape(size, size), cmap='gray', interpolation='nearest')
        plt.title(f'True: {true_labels[index]}\nPred: {predicted_labels[index]}', fontsize=10)
        plt.axis('off')
    plt.tight_layout()
    plt.show()

# Mostrar un número limitado de imágenes clasificadas incorrectamente (por ejemplo, 10)
num_to_show = min(10, len(incorrect_images))
plot_incorrect_predictions(incorrect_images[:num_to_show], incorrect_labels[:num_to_show], predicted_labels[:num_to_show])