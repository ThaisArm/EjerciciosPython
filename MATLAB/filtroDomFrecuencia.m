clc, clear, close all

%Leer imagen
img = imread("Manzana.jpg");
subplot(2,2,1);
imshow(img)
title("Imagen Original")

%Transformar a escala de grises
imgGray = rgb2gray(img);

%Dar ruido a la imagen
imgNoise = imnoise(imgGray, 'salt & pepper', 0.5);
subplot(2,2,2);
imshow(imgNoise)
title("Imagen con Ruido")

% Aplicar la transformada de Fourier
imgFFT = fftshift(fft2(imgNoise));
subplot(2,2,3);
imshow(imgFFT)

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
figure(2)
imshow(filteredFFT)

% Aplicar la transformada inversa de Fourier
filteredImg = real(ifft2(ifftshift(filteredFFT)));

% Mostrar la imagen original y la imagen filtrada
subplot(2,2,4);
imshow(filteredImg,[])
title("Filtro Fourier")