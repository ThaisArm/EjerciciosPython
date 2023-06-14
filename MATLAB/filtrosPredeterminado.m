clc, clear, close all

%Leer imagen
img = imread("Manzana.jpg");
subplot(2,3,1);
imshow(img)
title("Imagen Original")

%Transformar a escala de grises
imgGray = rgb2gray(img);

%Dar ruido a la imagen
imgNoise = imnoise(imgGray, 'salt & pepper', 0.5);
subplot(2,3,2);
imshow(imgNoise)
title("Imagen con Ruido")

%FILTROS DE MATLAB
%Filtro bilateral
sigma_spatial = 5; % Parámetro de desviación estándar para la similitud espacial
sigma_range = 0.2; % Parámetro de desviación estándar para la similitud en intensidad
imgBilateral = imbilatfilt(imgNoise, sigma_spatial, sigma_range);
subplot(2,3,3);
imshow(imgBilateral);
title("Filtro Bilateral")
%Filtro de promedio
imgFilterMean = filter2(fspecial('average',3),imgNoise)/255;
subplot(2,3,4);
imshow(imgFilterMean)
title("Filtro de Promedio")
%Filtro Gaussiano
sigma = 2; % Desviación estándar
imgGaussian = imgaussfilt(imgNoise, sigma);
subplot(2,3,5);
imshow(imgGaussian)
title("Filtro Gaussiano")
%Filtro de Mediana
imgMedian = medfilt2(imgNoise);
subplot(2,3,6);
imshow(imgMedian)
title("Filtro de Mediana")
