from random import randint
"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """Abstract parent class for melon orders"""

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        base_price = randint(5, 9)
        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price = base_price*1.5

        total = (1 + self.tax) * self.qty * base_price

        if hasattr(self, 'country_code') is True and self.qty < 10:
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        self.country_code = country_code
        return super(InternationalMelonOrder, self).__init__(species, qty)

    def get_country_code(self, country_code):
        """Return the country code."""

        return country_code


class GovMelonOrder(AbstractMelonOrder):
    """ Gov melon order with no tax, must pass inspection"""
    order_type = "government"
    passed_inspection = False
    tax = 0

    def mark_inspection(self, passed_inspection):
        self.passed_inspection = passed_inspection
        return passed_inspection
