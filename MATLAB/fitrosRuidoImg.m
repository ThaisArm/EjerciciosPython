clc
close all
clear all

%Leer imagen
img = imread("Manzana.jpg");
figure(1)
imshow(img)
title("Imagen Original")

%Transformar a escala de grises
imgGray = rgb2gray(img);

%Dar ruido a la imagen
imgNoise = imnoise(imgGray, 'salt & pepper', 0.5);
figure(2)
imshow(imgNoise)
title("Imagen con Ruido")

%FILTROS DE MATLAB
%Filtro bilateral
sigma_spatial = 5; % Parámetro de desviación estándar para la similitud espacial
sigma_range = 0.2; % Parámetro de desviación estándar para la similitud en intensidad
imgBilateral = imbilatfilt(imgNoise, sigma_spatial, sigma_range);
figure(3);
imshow(imgBilateral);
title("Filtro Bilateral")
%Filtro de promedio
imgFilterMean = filter2(fspecial('average',3),imgNoise)/255;
figure(4)
imshow(imgFilterMean)
title("Filtro de Promedio")
%Filtro Gaussiano
sigma = 2; % Desviación estándar
imgGaussian = imgaussfilt(imgNoise, sigma);
figure(5)
imshow(imgGaussian)
title("Filtro Gaussiano")
%Filtro de Mediana
imgMedian = medfilt2(imgNoise);
figure(6)
imshow(imgMedian)
title("Filtro de Mediana")

%FILTRO PROPIO


%FFT

% Aplicar la transformada de Fourier
imgFFT = fftshift(fft2(imgNoise));

% Calcular las dimensiones de la imagen y el centro del espectro
[m, n] = size(imgNoise);
center = [ceil(m/2), ceil(n/2)];

% Definir el radio del filtro de paso bajo
radius = 90;

% Crear el filtro de paso bajo en el dominio de la frecuencia
lowPassFilter = zeros(m, n);
for i = 1:m
    for j = 1:n
        distance = sqrt((i - center(1))^2 + (j - center(2))^2);
        if distance <= radius
            lowPassFilter(i, j) = 1;
        end
    end
end

% Aplicar el filtro de paso bajo en el dominio de la frecuencia
filteredFFT = imgFFT .* lowPassFilter;
figure(9)
imshow(filteredFFT)

% Aplicar la transformada inversa de Fourier
filteredImg = real(ifft2(ifftshift(filteredFFT)));

% Mostrar la imagen original y la imagen filtrada
figure(10)
imshow(filteredImg,[])
title("Filtro Fourier")
