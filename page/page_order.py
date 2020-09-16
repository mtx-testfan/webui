import page
from base1.base import Base


class PageOrder(Base):
    def page_click_right_cart(self):
        self.base_click(page.order_click_cart)

    def page_click_first_good(self):
        self.base_click(page.order_click_first_good)

    def page_click_pay_button(self):
        self.base_click(page.order_click_pay)

    def page_click_payment(self):
        self.base_click(page.order_goods_to_pay)

    def page_click_submit(self):
        self.base_click(page.order_click_submit)

    def page_order(self):
        # 点击首页右上角的购物车
        self.page_click_right_cart()

        # 点击第一个商品
        self.page_click_first_good()
        # 点击结算按钮
        self.page_click_pay_button()
        # 选择付款方式
        self.page_click_payment()
        # 提交订单
        self.page_click_submit()