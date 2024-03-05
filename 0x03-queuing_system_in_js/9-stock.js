import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();

const listProducts = [
    { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
    { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
    { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
    { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

const getItemById = (id) => {
    return listProducts.find(product => product.itemId === id);
};

const reserveStockById = async (itemId, stock) => {
    const setAsync = promisify(client.set).bind(client);
    await setAsync(`item.${itemId}`, stock.toString());
};

const getCurrentReservedStockById = async (itemId) => {
    const getAsync = promisify(client.get).bind(client);
    const reservedStock = await getAsync(`item.${itemId}`);
    return reservedStock ? parseInt(reservedStock) : 0;
};

app.get('/list_products', (req, res) => {
    res.json(listProducts.map(product => ({
        itemId: product.itemId,
        itemName: product.itemName,
        price: product.price,
        initialAvailableQuantity: product.initialAvailableQuantity
    })));
});

app.get('/list_products/:itemId', async (req, res) => {
    const { itemId } = req.params;
    const product = getItemById(parseInt(itemId));
    if (!product) {
        return res.json({ status: 'Product not found' });
    }
    const currentQuantity = product.initialAvailableQuantity - await getCurrentReservedStockById(parseInt(itemId));
    res.json({ ...product, currentQuantity });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const { itemId } = req.params;
    const product = getItemById(parseInt(itemId));
    if (!product) {
        return res.json({ status: 'Product not found' });
    }
    const currentStock = product.initialAvailableQuantity - await getCurrentReservedStockById(parseInt(itemId));
    if (currentStock <= 0) {
        return res.json({ status: 'Not enough stock available', itemId: product.itemId });
    }
    await reserveStockById(parseInt(itemId), currentStock - 1);
    res.json({ status: 'Reservation confirmed', itemId: product.itemId });
});

app.listen(1245, () => {
    console.log('Server is running on port 1245');
});
