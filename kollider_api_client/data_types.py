import uuid

class Order(object):
	'''
	Order object
		side: Bid | Ask
		margin_type: Isolated | More comming (maybe)
		settlement_type: Instant | Delayed
		price: unsigned int
		quantity: unsigned int
		leverage: unsigned int
	'''
	symbol: str = ""
	quantity: int = 1
	leverage: int = 100
	side: str = "Bid"
	price: int = 400000
	# ext_order_id: str = str(uuid.uuid4())
	order_type: str = "Limit"
	margin_type: str = "Isolated"
	settlement_type: str = "Instant"

	def to_dict(self):
		return {
			"price": self.price,
			"order_type": self.order_type,
			"side": self.side,
			"quantity": self.quantity,
			"symbol": self.symbol,
			"leverage": self.leverage,
			# "ext_order_id": self.ext_order_id,
			"margin_type": self.margin_type,
			"settlement_type": self.settlement_type
		}


if __name__ in "__main__":
	None
