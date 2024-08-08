CREATE TRIGGER quantity_update AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.NUMBER
WHERE name = NEW.item_name;
