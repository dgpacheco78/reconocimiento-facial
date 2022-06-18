from deepface import DeepFace

obj = DeepFace.analyze(img_path = "/home/pacheco/Imágenes/mayra.jpg", actions = ['age', 'gender', 'race', 'emotion'])

print(obj)