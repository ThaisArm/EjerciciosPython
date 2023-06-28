clc, clear, close all

% Leer la imagen original en color
imagen_original = imread(['Manzana.jpg']);

% Convertir la imagen a escala de grises
imgGray = rgb2gray(imagen_original);
imgNoise = imnoise(imgGray, 'salt & pepper', 0.5);

% Obtener las dimensiones de la imagen
[filas, columnas] = size(imgNoise);

% Definir el filtro de suavizado
filtro = double([1, 1, 1; 1, 1, 1; 1, 1, 1]); % Convertir el filtro a tipo double

% Agregar un padding de ceros a la imagen
imagen_padded = padarray(imgNoise, [1, 1], 0, 'both');

% Crear una imagen vacía para almacenar el resultado de la convolución
imagen_suavizada = zeros(filas, columnas);

% Realizar la convolución de manera manual
for i = 2 : filas + 1
    for j = 2 : columnas + 1
        % Extraer la región de la imagen correspondiente al filtro
        region = double(imagen_padded(i-1:i+1, j-1:j+1)); % Convertir la región a tipo double
        
        % Realizar la convolución multiplicando elemento a elemento y sumando
        resultado = region .* filtro;

        % Calcular la mediana de la región filtrada
        mediana = median(resultado(:));
        
        % Asignar el valor resultante al píxel correspondiente en la imagen suavizada
        imagen_suavizada(i-1, j-1) = mediana;
    end
end

% Definir segundo filtro de suavizado
filtro_2 = double([2, -1, 2; 1, 0, 1; 2, -1, 2]); % Convertir el filtro a tipo double

% Agregar un padding de ceros a la imagen
imagen_padded = padarray(imagen_suavizada, [1, 1], 0, 'both');

% Crear una imagen vacía para almacenar el resultado de la convolución
imagen_suavizada_2 = zeros(filas, columnas);

% Realizar la convolución de manera manual
for i = 2 : filas + 1
    for j = 2 : columnas + 1
        % Extraer la región de la imagen correspondiente al filtro
        region = double(imagen_padded(i-1:i+1, j-1:j+1)); % Convertir la región a tipo double
        
        % Realizar la convolución multiplicando elemento a elemento y sumando
        resultado = region .* filtro_2;

        % Calcular la mediana de la región filtrada
        prom = mean(resultado(:));
        
        % Asignar el valor resultante al píxel correspondiente en la imagen suavizada
        imagen_suavizada_2(i-1, j-1) = prom;
    end
end

% Mostrar la imagen original y la imagen suavizada
figure(1)
%subplot(1, 2, 1);
imshow(imgGray);
%title('Imagen Original');
%subplot(1, 2, 2);
figure(2)
imshow(uint8(imagen_suavizada_2));
title('Imagen Suavizada');
