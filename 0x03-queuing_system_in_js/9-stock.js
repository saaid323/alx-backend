import express from 'express';
import redis from 'redis';
const {promisify} = require('util');
const listProducts = [
	{
		id: 1,
		name: 'Suitcase 250',
		price: 50,
		stock: 4
  	},
  	{
		id: 2,
    		name: 'Suitcase 450',
    		price: 100,
    		stock: 10
  	},
  	{
    		id: 3,
    		name: 'Suitcase 650',
    		price: 350,
    		stock: 2
  	},
  	{
    		id: 4,
    		name: 'Suitcase 1050',
    		price: 550,
    		stock: 5
  	},
]

const app = express();
app.listen(1245);
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

const getItemById = (id) => {
    return listProducts.find(product => product.id === id);
};

function reserveStockById(itemId, stock) {
	client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
	return await getAsync(itemId);
}


app.get('/list_products', (req, res) => {
        res.json(listProducts);
});

app.get('/list_products/:itemId', (req, res) => {
	const itemId = Number.parseInt(req.params.itemId);
	const item = getItemById(itemId);
	if (!item) {
		res.json({ status: 'Product not found' });
	}
	//getCurrentReservedStockById(itemId).then((result) => Number.parseInt(result || 0)).then((value) => res.json(value));
	const currentQuantity = item.initialAvailableQuantity;
	res.json({item, currentQuantity });
});


app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);
    if (!product) {
        res.status(404).json({ status: "Product not found" });
    } else {
        const currentStock = product.stock;
        if (currentStock <= 0) {
            res.json({ status: "Not enough stock available", itemId });
        } else {
            await reserveStockById(itemId, currentStock - 1);
            res.json({ status: "Reservation confirmed", itemId });
        }
    }
});

