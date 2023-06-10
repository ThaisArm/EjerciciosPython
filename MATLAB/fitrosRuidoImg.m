clc
close all
clear all

%Leer imagen
img = imread("Manzana.jpg");
figure(1)
imshow(img)

%Transformar a escala de grises
imgGray = rgb2gray(img);

%Dar ruido a la imagen
imgNoise = imnoise(imgGray, 'salt & pepper', 0.5);
figure(2)
imshow(imgNoise)

%FILTROS DE MATLAB
%Filtro de promedio
imgFilterMean = filter2(fspecial('average',3),imgNoise)/255;
figure(3)
imshow(imgFilterMean)
%Filtro bilateral
sigma_spatial = 5; % Parámetro de desviación estándar para la similitud espacial
sigma_range = 0.2; % Parámetro de desviación estándar para la similitud en intensidad
imgBilateral = imbilatfilt(imgNoise, sigma_spatial, sigma_range);
figure(6);
imshow(imgBilateral);
%Filtro Gaussiano
imgGaussian = imgaussfilt(imgNoise);
figure(5);
imshow(imgGaussian);
%Filtro de Wiener
imgWiener = wiener2(imgNoise);
figure(7);
imshow(imgWiener);
%Filtro de Mediana
imgMedian = medfilt2(imgNoise);
figure(4)
imshow(imgMedian)

%FILTRO PROPIO

%FFT



