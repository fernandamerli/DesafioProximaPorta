# Desafio Próxima Porta

## Motivação
#### Desenvolvi o código em Django, conforme sugerido, e utilizei o Django Rest Framework para as APIs. Para a persistência dos mapas, fiz integração com o MySQL e estruturei os dados em duas tabelas. Por fim, utilizei o pytest para testar as requisições.
#### Por serem ferramentas novas para mim, tive algumas dificuldades durante o desenvolvimento da solução, mas gostei bastante de ter sido desafiada!

## APIs desenvolvidas para o desafio proposto

### *delivery_list*: recuperar e popular a base de dados
#### Métodos: GET e POST
#### URL: api/deliveries
#### Parâmetros
      map_name: string
      routes: array
      origin: string
      destination: string
      distance: int
#### Exemplo requisição GET:
      api/deliveries?map_name=mapa
#### Exemplo requisição POST: 
      {
          "map_name": "mapa",
          "routes": [
              {
                  "origin": "a",
                  "destination": "b",
                  "distance": 10
              },
              {
                  "origin": "b",
                  "destination": "d",
                  "distance": 15
              },
              {
                  "origin": "a",
                  "destination": "c",
                  "distance": 20
              },
              {
                  "origin": "c",
                  "destination": "d",
                  "distance": 30
              },
              {
                  "origin": "b",
                  "destination": "e",
                  "distance": 50
              },
              {
                  "origin": "d",
                  "destination": "e",
                  "distance": 30
              }
          ]
      }

### *delivery_process*: procurar o menor valor de entrega e seu caminho
#### Método: POST
#### URL: api/deliveries/best_route
#### Parâmetros
      map_name: string
      origin: string
      destination: string
      truck_range: int
      fuel_cost: decimal
#### Exemplo requisição POST: 
      {
          "map_name": "mapa",
          "origin": "a",
          "destination": "d",
          "truck_range": 10,
          "fuel_cost": 2.5
      }
 
## Testes das APIs
Arquivo: deliveries\tests.py
