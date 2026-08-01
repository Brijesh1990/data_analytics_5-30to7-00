from database.connection import DatabaseManager
from utils.logger import logger

class SalesReport:
    """Sales Report Model for generating daily, weekly, monthly, and custom period analytics."""

    @classmethod
    def get_summary_stats(cls, period="today"):
        """
        Retrieves total sales, order count, average order value, and tax collected.
        period options: 'today', 'weekly', 'monthly', 'all'
        """
        date_filter = ""
        if period == "today":
            date_filter = "AND DATE(created_at) = CURRENT_DATE()"
        elif period == "weekly":
            date_filter = "AND created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)"
        elif period == "monthly":
            date_filter = "AND created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)"

        query = f"""
            SELECT 
                COUNT(*) AS total_orders,
                COALESCE(SUM(grand_total), 0.00) AS total_revenue,
                COALESCE(AVG(grand_total), 0.00) AS avg_order_value,
                COALESCE(SUM(tax_amount), 0.00) AS total_tax,
                COALESCE(SUM(discount_amount), 0.00) AS total_discount
            FROM orders
            WHERE order_status = 'completed' {date_filter}
        """
        try:
            return DatabaseManager.execute_query(query, fetch_one=True)
        except Exception as e:
            logger.error(f"Error fetching summary stats for period '{period}': {e}")
            return {"total_orders": 0, "total_revenue": 0.0, "avg_order_value": 0.0, "total_tax": 0.0, "total_discount": 0.0}

    @classmethod
    def get_payment_breakdown(cls, period="today"):
        """Breakdown of revenue by payment mode (Cash, UPI, Card)."""
        date_filter = ""
        if period == "today":
            date_filter = "AND DATE(created_at) = CURRENT_DATE()"
        elif period == "weekly":
            date_filter = "AND created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)"
        elif period == "monthly":
            date_filter = "AND created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)"

        query = f"""
            SELECT 
                payment_method,
                COUNT(*) AS count,
                COALESCE(SUM(grand_total), 0.00) AS total_amount
            FROM orders
            WHERE order_status = 'completed' {date_filter}
            GROUP BY payment_method
        """
        try:
            return DatabaseManager.execute_query(query, fetch_all=True) or []
        except Exception as e:
            logger.error(f"Error fetching payment breakdown for period '{period}': {e}")
            return []

    @classmethod
    def get_top_selling_items(cls, period="today", limit=10):
        """Top items sold by quantity and total revenue."""
        date_filter = ""
        if period == "today":
            date_filter = "AND DATE(o.created_at) = CURRENT_DATE()"
        elif period == "weekly":
            date_filter = "AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)"
        elif period == "monthly":
            date_filter = "AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)"

        query = f"""
            SELECT 
                oi.item_name,
                c.name AS category_name,
                SUM(oi.quantity) AS total_qty,
                SUM(oi.subtotal) AS total_sales
            FROM order_items oi
            JOIN orders o ON oi.order_id = o.id
            LEFT JOIN menu_items m ON oi.menu_item_id = m.id
            LEFT JOIN categories c ON m.category_id = c.id
            WHERE o.order_status = 'completed' {date_filter}
            GROUP BY oi.item_name, c.name
            ORDER BY total_qty DESC
            LIMIT {int(limit)}
        """
        try:
            return DatabaseManager.execute_query(query, fetch_all=True) or []
        except Exception as e:
            logger.error(f"Error fetching top selling items for period '{period}': {e}")
            return []

    @classmethod
    def get_sales_trend(cls, period="monthly"):
        """Daily sales trend for graph/table plotting."""
        if period == "monthly":
            days = 30
        elif period == "weekly":
            days = 7
        else:
            days = 1

        query = f"""
            SELECT 
                DATE(created_at) AS sale_date,
                COUNT(*) AS order_count,
                SUM(grand_total) AS daily_revenue
            FROM orders
            WHERE order_status = 'completed' 
              AND created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL {days} DAY)
            GROUP BY DATE(created_at)
            ORDER BY sale_date ASC
        """
        try:
            return DatabaseManager.execute_query(query, fetch_all=True) or []
        except Exception as e:
            logger.error(f"Error fetching sales trend: {e}")
            return []
