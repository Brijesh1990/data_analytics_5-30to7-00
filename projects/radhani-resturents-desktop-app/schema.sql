-- =======================================================
-- RAJDHANI RESTAURANT POS & BILLING SYSTEM SCHEMA
-- Database: rajdhani_pos_db
-- =======================================================

CREATE DATABASE IF NOT EXISTS `rajdhani_pos_db` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `rajdhani_pos_db`;

-- 1. USERS TABLE (Admin & Cashier Authentication)
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(50) NOT NULL UNIQUE,
    `password_hash` VARCHAR(255) NOT NULL,
    `full_name` VARCHAR(100) NOT NULL,
    `role` ENUM('admin', 'cashier') NOT NULL DEFAULT 'cashier',
    `phone` VARCHAR(20) DEFAULT NULL,
    `is_active` TINYINT(1) DEFAULT 1,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. CATEGORIES TABLE
CREATE TABLE IF NOT EXISTS `categories` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL UNIQUE,
    `display_order` INT DEFAULT 0,
    `is_active` TINYINT(1) DEFAULT 1,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. MENU ITEMS TABLE
CREATE TABLE IF NOT EXISTS `menu_items` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `category_id` INT NOT NULL,
    `item_code` VARCHAR(20) UNIQUE NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `price` DECIMAL(10, 2) NOT NULL,
    `description` TEXT DEFAULT NULL,
    `food_type` ENUM('veg', 'non-veg') NOT NULL DEFAULT 'veg',
    `stock_quantity` INT DEFAULT 100,
    `is_inventory_tracked` TINYINT(1) DEFAULT 0,
    `is_available` TINYINT(1) DEFAULT 1,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. CUSTOMERS TABLE
CREATE TABLE IF NOT EXISTS `customers` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `phone` VARCHAR(15) NOT NULL UNIQUE,
    `email` VARCHAR(100) DEFAULT NULL,
    `address` TEXT DEFAULT NULL,
    `total_visits` INT DEFAULT 1,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5. ORDERS TABLE
CREATE TABLE IF NOT EXISTS `orders` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `bill_number` VARCHAR(30) UNIQUE NOT NULL,
    `customer_id` INT DEFAULT NULL,
    `user_id` INT NOT NULL,
    `dining_type` ENUM('table', 'takeaway', 'delivery') NOT NULL DEFAULT 'table',
    `table_number` VARCHAR(20) DEFAULT 'Takeaway',
    `subtotal` DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    `discount_type` ENUM('percent', 'flat') DEFAULT 'flat',
    `discount_value` DECIMAL(10, 2) DEFAULT 0.00,
    `discount_amount` DECIMAL(10, 2) DEFAULT 0.00,
    `tax_rate` DECIMAL(5, 2) DEFAULT 5.00,
    `tax_amount` DECIMAL(10, 2) DEFAULT 0.00,
    `grand_total` DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    `payment_method` ENUM('cash', 'card', 'upi') NOT NULL DEFAULT 'cash',
    `payment_status` ENUM('paid', 'pending', 'refunded') NOT NULL DEFAULT 'paid',
    `order_status` ENUM('completed', 'cancelled') NOT NULL DEFAULT 'completed',
    `notes` TEXT DEFAULT NULL,
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE SET NULL,
    FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 6. ORDER ITEMS TABLE
CREATE TABLE IF NOT EXISTS `order_items` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `order_id` INT NOT NULL,
    `menu_item_id` INT DEFAULT NULL,
    `item_name` VARCHAR(100) NOT NULL,
    `unit_price` DECIMAL(10, 2) NOT NULL,
    `quantity` INT NOT NULL DEFAULT 1,
    `subtotal` DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`menu_item_id`) REFERENCES `menu_items` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 7. PAYMENTS TABLE
CREATE TABLE IF NOT EXISTS `payments` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `order_id` INT NOT NULL,
    `payment_method` ENUM('cash', 'card', 'upi') NOT NULL,
    `amount_paid` DECIMAL(10, 2) NOT NULL,
    `transaction_ref` VARCHAR(100) DEFAULT NULL,
    `payment_date` DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 8. SETTINGS TABLE
CREATE TABLE IF NOT EXISTS `settings` (
    `setting_key` VARCHAR(50) PRIMARY KEY,
    `setting_value` TEXT NOT NULL,
    `description` VARCHAR(255) DEFAULT NULL,
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- =======================================================
-- SEED DATA INSERTION
-- Default Users:
-- Admin: admin / admin123 (SHA-256: 240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9)
-- Cashier: cashier / cashier123 (SHA-256: b4c94003c562bb0d89535eca77f07284fe560fd48a7cc1ed99f0a56263d616ba)
-- =======================================================

INSERT INTO `users` (`username`, `password_hash`, `full_name`, `role`, `phone`) VALUES
('admin', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 'Rajdhani Admin', 'admin', '9876543210'),
('cashier', 'b4c94003c562bb0d89535eca77f07284fe560fd48a7cc1ed99f0a56263d616ba', 'Main Cashier', 'cashier', '9876543211')
ON DUPLICATE KEY UPDATE `password_hash`=VALUES(`password_hash`), `full_name`=VALUES(`full_name`), `role`=VALUES(`role`);

-- Seed Categories
INSERT INTO `categories` (`id`, `name`, `display_order`) VALUES
(1, 'Breakfast', 1),
(2, 'Rajdhani Special Thali', 2),
(3, 'Starters & Snacks', 3),
(4, 'Main Course (Veg)', 4),
(5, 'Main Course (Non-Veg)', 5),
(6, 'Breads & Rice', 6),
(7, 'Beverages & Drinks', 7),
(8, 'Desserts & Sweets', 8)
ON DUPLICATE KEY UPDATE `name`=`name`;

-- Seed Menu Items
INSERT INTO `menu_items` (`category_id`, `item_code`, `name`, `price`, `description`, `food_type`, `stock_quantity`, `is_inventory_tracked`) VALUES
-- Breakfast
(1, 'BF101', 'Masala Dosa', 140.00, 'Crispy rice crepe served with spiced potato filing & sambar', 'veg', 100, 1),
(1, 'BF102', 'Idli Sambar (2 Pcs)', 90.00, 'Steamed rice cakes with chutney and sambar', 'veg', 100, 1),
(1, 'BF103', 'Puri Bhaji', 120.00, 'Fluffy deep-fried bread with spicy potato curry', 'veg', 100, 1),
(1, 'BF104', 'Poha Special', 80.00, 'Flattened rice cooked with mustard, peanuts and curry leaves', 'veg', 100, 1),
(1, 'BF105', 'Chole Bhature', 160.00, 'Rich chickpea curry served with two large fluffy bhaturas', 'veg', 100, 1),

-- Rajdhani Special Thali
(2, 'TH201', 'Rajdhani Royal Grand Thali', 350.00, 'Complete royal feast: 3 Sabzi, Dal Tadka, Paneer, Gulab Jamun, Rice, 4 Roti, Salad', 'veg', 80, 1),
(2, 'TH202', 'Executive Veg Thali', 240.00, 'Paneer Butter Masala, Dal Makhani, Jeera Rice, 3 Butter Roti, Sweet', 'veg', 80, 1),
(2, 'TH203', 'Royal Non-Veg Deluxe Thali', 390.00, 'Butter Chicken, Mutton Curry, Dal, Biryani Rice, 3 Naan, Gulab Jamun', 'non-veg', 50, 1),

-- Starters & Snacks
(3, 'SN301', 'Paneer Tikka Grill', 240.00, 'Marinated paneer cubes grilled in clay tandoor', 'veg', 60, 1),
(3, 'SN302', 'Veg Spring Roll', 180.00, 'Crispy rolls stuffed with julienned vegetables', 'veg', 60, 1),
(3, 'SN303', 'Chicken Tandoori Half', 320.00, 'Classic smoky tandoori chicken marinated in yogurt and spices', 'non-veg', 50, 1),
(3, 'SN304', 'Hara Bhara Kebab', 190.00, 'Pan-fried spinach and green pea patties', 'veg', 60, 1),
(3, 'SN305', 'Crispy Corn Salt & Pepper', 170.00, 'Fried sweet corn tossed with capsicum and pepper', 'veg', 60, 1),

-- Main Course Veg
(4, 'MC401', 'Paneer Butter Masala', 280.00, 'Soft paneer in rich creamy tomato cashew gravy', 'veg', 100, 1),
(4, 'MC402', 'Dal Makhani Special', 230.00, 'Slow cooked black lentils simmered overnight with cream', 'veg', 100, 1),
(4, 'MC403', 'Kaju Curry', 310.00, 'Roasted cashews simmered in royal mughlai gravy', 'veg', 100, 1),
(4, 'MC404', 'Kadhai Paneer', 270.00, 'Paneer cooked with bell peppers and whole coriander spices', 'veg', 100, 1),
(4, 'MC405', 'Mix Vegetable Handi', 220.00, 'Seasonal garden vegetables cooked in aromatic thick gravy', 'veg', 100, 1),

-- Main Course Non-Veg
(5, 'MN501', 'Butter Chicken Boneless', 360.00, 'Tender chicken pieces in rich tomato cream butter gravy', 'non-veg', 50, 1),
(5, 'MN502', 'Chicken Tikka Masala', 340.00, 'Tandoori chicken tikka cooked in spicy onion gravy', 'non-veg', 50, 1),
(5, 'MN503', 'Mughlai Mutton Rongan Josh', 420.00, 'Slow cooked tender mutton in aromatic Kashmiri spices', 'non-veg', 40, 1),

-- Breads & Rice
(6, 'BR601', 'Butter Naan', 50.00, 'Soft tandoori naan brushed with fresh butter', 'veg', 200, 1),
(6, 'BR602', 'Garlic Butter Naan', 65.00, 'Naan topped with chopped garlic and coriander', 'veg', 200, 1),
(6, 'BR603', 'Tandoori Roti', 25.00, 'Whole wheat flatbread baked in clay tandoor', 'veg', 300, 1),
(6, 'BR604', 'Veg Dum Biryani', 220.00, 'Fragrant basmati rice layered with vegetables and saffron', 'veg', 80, 1),
(6, 'BR605', 'Hyderabadi Chicken Biryani', 310.00, 'Authentic layered chicken biryani with mirchi ka salan', 'non-veg', 80, 1),
(6, 'BR606', 'Jeera Rice', 140.00, 'Basmati rice tempered with cumin seeds and ghee', 'veg', 100, 1),

-- Beverages
(7, 'BV701', 'Masala Special Tea', 35.00, 'Indian spiced milk tea brewed with cardamom and ginger', 'veg', 300, 1),
(7, 'BV702', 'Filter Coffee', 45.00, 'South Indian style aromatic drip filter coffee', 'veg', 300, 1),
(7, 'BV703', 'Fresh Sweet Lassi', 80.00, 'Thick chilled yogurt drink topped with malai and nuts', 'veg', 100, 1),
(7, 'BV704', 'Fresh Lime Soda', 60.00, 'Refreshing lime juice with sparkling soda water', 'veg', 100, 1),
(7, 'BV705', 'Badam Milk Chilled', 95.00, 'Cold saffron almond milk enriched with pistachio', 'veg', 100, 1),

-- Desserts
(8, 'DS801', 'Gulab Jamun (2 Pcs)', 90.00, 'Soft fried milk solids soaked in rose scented sugar syrup', 'veg', 100, 1),
(8, 'DS802', 'Rasmalai (2 Pcs)', 110.00, 'Soft cottage cheese patties in cardamom saffron milk', 'veg', 100, 1),
(8, 'DS803', 'Matka Kulfi', 100.00, 'Traditional rich frozen dessert served in clay pot', 'veg', 100, 1),
(8, 'DS804', 'Sizzling Brownie with Ice Cream', 190.00, 'Warm chocolate brownie topped with vanilla ice cream and fudge', 'veg', 60, 1)
ON DUPLICATE KEY UPDATE `item_code`=`item_code`;

-- Seed Default Settings
INSERT INTO `settings` (`setting_key`, `setting_value`, `description`) VALUES
('restaurant_name', 'Rajdhani Restaurant', 'Official Name of Restaurant'),
('tagline', 'Authentic Indian Flavors & Fine Dining', 'Tagline printed on invoice'),
('address', '123 Heritage Palace Road, Near City Center, New Delhi - 110001', 'Restaurant Address'),
('phone', '+91 98765 43210', 'Contact Phone Number'),
('email', 'contact@rajdhanirestaurant.com', 'Contact Email'),
('gstin', '07AAAAA0000A1Z5', 'GSTIN Tax Registration Number'),
('tax_rate', '5.0', 'Total GST Percentage (%)'),
('enable_tax', 'true', 'Tax Enabled Toggle'),
('currency_symbol', '₹', 'Currency Symbol'),
('receipt_footer', 'Thank you for dining with Rajdhani Restaurant! Visit Again!', 'Invoice Footer Message')
ON DUPLICATE KEY UPDATE `setting_key`=`setting_key`;
