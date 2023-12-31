# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from oip_api_server.models.base_model_ import Model
from oip_api_server import util


class CountriesBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, code: str=None, eu_country_region_code: str=None, intrastat_code: str=None, address_format: str=None, contact_address_format: str=None, global_dimension2_code: str=None, customer_template_code: str=None, income_cost_carrier_code: str=None, eu_affiliation: str=None, continent: str=None, max_iban_length: str=None, length_of_bank_branch_code: str=None, responsibility_center: str=None, iso_code: str=None, culture_info: str=None, signature: str=None, primary_language_code: str=None, bank_country_code: str=None, eu_standard: str=None, invoicing_in_local_currency: str=None, currency_code: str=None, default_length_branch_code: str=None, default_length_account_no: str=None, iso_bank_code: str=None, accounting_period: str=None, vat_registration_obligation: str=None, vend_gen_bus_posting_group: str=None, cust_gen_bus_posting_group: str=None, tenant: str=None):  # noqa: E501
        """CountriesBody - a model defined in Swagger

        :param name: The name of this CountriesBody.  # noqa: E501
        :type name: str
        :param code: The code of this CountriesBody.  # noqa: E501
        :type code: str
        :param eu_country_region_code: The eu_country_region_code of this CountriesBody.  # noqa: E501
        :type eu_country_region_code: str
        :param intrastat_code: The intrastat_code of this CountriesBody.  # noqa: E501
        :type intrastat_code: str
        :param address_format: The address_format of this CountriesBody.  # noqa: E501
        :type address_format: str
        :param contact_address_format: The contact_address_format of this CountriesBody.  # noqa: E501
        :type contact_address_format: str
        :param global_dimension2_code: The global_dimension2_code of this CountriesBody.  # noqa: E501
        :type global_dimension2_code: str
        :param customer_template_code: The customer_template_code of this CountriesBody.  # noqa: E501
        :type customer_template_code: str
        :param income_cost_carrier_code: The income_cost_carrier_code of this CountriesBody.  # noqa: E501
        :type income_cost_carrier_code: str
        :param eu_affiliation: The eu_affiliation of this CountriesBody.  # noqa: E501
        :type eu_affiliation: str
        :param continent: The continent of this CountriesBody.  # noqa: E501
        :type continent: str
        :param max_iban_length: The max_iban_length of this CountriesBody.  # noqa: E501
        :type max_iban_length: str
        :param length_of_bank_branch_code: The length_of_bank_branch_code of this CountriesBody.  # noqa: E501
        :type length_of_bank_branch_code: str
        :param responsibility_center: The responsibility_center of this CountriesBody.  # noqa: E501
        :type responsibility_center: str
        :param iso_code: The iso_code of this CountriesBody.  # noqa: E501
        :type iso_code: str
        :param culture_info: The culture_info of this CountriesBody.  # noqa: E501
        :type culture_info: str
        :param signature: The signature of this CountriesBody.  # noqa: E501
        :type signature: str
        :param primary_language_code: The primary_language_code of this CountriesBody.  # noqa: E501
        :type primary_language_code: str
        :param bank_country_code: The bank_country_code of this CountriesBody.  # noqa: E501
        :type bank_country_code: str
        :param eu_standard: The eu_standard of this CountriesBody.  # noqa: E501
        :type eu_standard: str
        :param invoicing_in_local_currency: The invoicing_in_local_currency of this CountriesBody.  # noqa: E501
        :type invoicing_in_local_currency: str
        :param currency_code: The currency_code of this CountriesBody.  # noqa: E501
        :type currency_code: str
        :param default_length_branch_code: The default_length_branch_code of this CountriesBody.  # noqa: E501
        :type default_length_branch_code: str
        :param default_length_account_no: The default_length_account_no of this CountriesBody.  # noqa: E501
        :type default_length_account_no: str
        :param iso_bank_code: The iso_bank_code of this CountriesBody.  # noqa: E501
        :type iso_bank_code: str
        :param accounting_period: The accounting_period of this CountriesBody.  # noqa: E501
        :type accounting_period: str
        :param vat_registration_obligation: The vat_registration_obligation of this CountriesBody.  # noqa: E501
        :type vat_registration_obligation: str
        :param vend_gen_bus_posting_group: The vend_gen_bus_posting_group of this CountriesBody.  # noqa: E501
        :type vend_gen_bus_posting_group: str
        :param cust_gen_bus_posting_group: The cust_gen_bus_posting_group of this CountriesBody.  # noqa: E501
        :type cust_gen_bus_posting_group: str
        :param tenant: The tenant of this CountriesBody.  # noqa: E501
        :type tenant: str
        """
        self.swagger_types = {
            'name': str,
            'code': str,
            'eu_country_region_code': str,
            'intrastat_code': str,
            'address_format': str,
            'contact_address_format': str,
            'global_dimension2_code': str,
            'customer_template_code': str,
            'income_cost_carrier_code': str,
            'eu_affiliation': str,
            'continent': str,
            'max_iban_length': str,
            'length_of_bank_branch_code': str,
            'responsibility_center': str,
            'iso_code': str,
            'culture_info': str,
            'signature': str,
            'primary_language_code': str,
            'bank_country_code': str,
            'eu_standard': str,
            'invoicing_in_local_currency': str,
            'currency_code': str,
            'default_length_branch_code': str,
            'default_length_account_no': str,
            'iso_bank_code': str,
            'accounting_period': str,
            'vat_registration_obligation': str,
            'vend_gen_bus_posting_group': str,
            'cust_gen_bus_posting_group': str,
            'tenant': str
        }

        self.attribute_map = {
            'name': 'Name',
            'code': 'Code',
            'eu_country_region_code': 'EUCountryRegionCode',
            'intrastat_code': 'IntrastatCode',
            'address_format': 'AddressFormat',
            'contact_address_format': 'ContactAddressFormat',
            'global_dimension2_code': 'GlobalDimension2Code',
            'customer_template_code': 'CustomerTemplateCode',
            'income_cost_carrier_code': 'IncomeCostCarrierCode',
            'eu_affiliation': 'EUAffiliation',
            'continent': 'Continent',
            'max_iban_length': 'MaxIBANLength',
            'length_of_bank_branch_code': 'LengthOfBankBranchCode',
            'responsibility_center': 'ResponsibilityCenter',
            'iso_code': 'ISOCode',
            'culture_info': 'CultureInfo',
            'signature': 'Signature',
            'primary_language_code': 'PrimaryLanguageCode',
            'bank_country_code': 'BankCountryCode',
            'eu_standard': 'EUStandard',
            'invoicing_in_local_currency': 'InvoicingInLocalCurrency',
            'currency_code': 'CurrencyCode',
            'default_length_branch_code': 'DefaultLengthBranchCode',
            'default_length_account_no': 'DefaultLengthAccountNo',
            'iso_bank_code': 'ISOBankCode',
            'accounting_period': 'AccountingPeriod',
            'vat_registration_obligation': 'VATRegistrationObligation',
            'vend_gen_bus_posting_group': 'VendGenBusPostingGroup',
            'cust_gen_bus_posting_group': 'CustGenBusPostingGroup',
            'tenant': 'Tenant'
        }
        self._name = name
        self._code = code
        self._eu_country_region_code = eu_country_region_code
        self._intrastat_code = intrastat_code
        self._address_format = address_format
        self._contact_address_format = contact_address_format
        self._global_dimension2_code = global_dimension2_code
        self._customer_template_code = customer_template_code
        self._income_cost_carrier_code = income_cost_carrier_code
        self._eu_affiliation = eu_affiliation
        self._continent = continent
        self._max_iban_length = max_iban_length
        self._length_of_bank_branch_code = length_of_bank_branch_code
        self._responsibility_center = responsibility_center
        self._iso_code = iso_code
        self._culture_info = culture_info
        self._signature = signature
        self._primary_language_code = primary_language_code
        self._bank_country_code = bank_country_code
        self._eu_standard = eu_standard
        self._invoicing_in_local_currency = invoicing_in_local_currency
        self._currency_code = currency_code
        self._default_length_branch_code = default_length_branch_code
        self._default_length_account_no = default_length_account_no
        self._iso_bank_code = iso_bank_code
        self._accounting_period = accounting_period
        self._vat_registration_obligation = vat_registration_obligation
        self._vend_gen_bus_posting_group = vend_gen_bus_posting_group
        self._cust_gen_bus_posting_group = cust_gen_bus_posting_group
        self._tenant = tenant

    @classmethod
    def from_dict(cls, dikt) -> 'CountriesBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The countries_body of this CountriesBody.  # noqa: E501
        :rtype: CountriesBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this CountriesBody.

        The name of the country  # noqa: E501

        :return: The name of this CountriesBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this CountriesBody.

        The name of the country  # noqa: E501

        :param name: The name of this CountriesBody.
        :type name: str
        """

        self._name = name

    @property
    def code(self) -> str:
        """Gets the code of this CountriesBody.

        The code of the country  # noqa: E501

        :return: The code of this CountriesBody.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this CountriesBody.

        The code of the country  # noqa: E501

        :param code: The code of this CountriesBody.
        :type code: str
        """

        self._code = code

    @property
    def eu_country_region_code(self) -> str:
        """Gets the eu_country_region_code of this CountriesBody.

        The EU country/region code of the country  # noqa: E501

        :return: The eu_country_region_code of this CountriesBody.
        :rtype: str
        """
        return self._eu_country_region_code

    @eu_country_region_code.setter
    def eu_country_region_code(self, eu_country_region_code: str):
        """Sets the eu_country_region_code of this CountriesBody.

        The EU country/region code of the country  # noqa: E501

        :param eu_country_region_code: The eu_country_region_code of this CountriesBody.
        :type eu_country_region_code: str
        """

        self._eu_country_region_code = eu_country_region_code

    @property
    def intrastat_code(self) -> str:
        """Gets the intrastat_code of this CountriesBody.

        The Intrastat code of the country  # noqa: E501

        :return: The intrastat_code of this CountriesBody.
        :rtype: str
        """
        return self._intrastat_code

    @intrastat_code.setter
    def intrastat_code(self, intrastat_code: str):
        """Sets the intrastat_code of this CountriesBody.

        The Intrastat code of the country  # noqa: E501

        :param intrastat_code: The intrastat_code of this CountriesBody.
        :type intrastat_code: str
        """

        self._intrastat_code = intrastat_code

    @property
    def address_format(self) -> str:
        """Gets the address_format of this CountriesBody.

        The address format of the country  # noqa: E501

        :return: The address_format of this CountriesBody.
        :rtype: str
        """
        return self._address_format

    @address_format.setter
    def address_format(self, address_format: str):
        """Sets the address_format of this CountriesBody.

        The address format of the country  # noqa: E501

        :param address_format: The address_format of this CountriesBody.
        :type address_format: str
        """

        self._address_format = address_format

    @property
    def contact_address_format(self) -> str:
        """Gets the contact_address_format of this CountriesBody.

        The contact address format of the country  # noqa: E501

        :return: The contact_address_format of this CountriesBody.
        :rtype: str
        """
        return self._contact_address_format

    @contact_address_format.setter
    def contact_address_format(self, contact_address_format: str):
        """Sets the contact_address_format of this CountriesBody.

        The contact address format of the country  # noqa: E501

        :param contact_address_format: The contact_address_format of this CountriesBody.
        :type contact_address_format: str
        """

        self._contact_address_format = contact_address_format

    @property
    def global_dimension2_code(self) -> str:
        """Gets the global_dimension2_code of this CountriesBody.

        The global dimension 2 code of the country  # noqa: E501

        :return: The global_dimension2_code of this CountriesBody.
        :rtype: str
        """
        return self._global_dimension2_code

    @global_dimension2_code.setter
    def global_dimension2_code(self, global_dimension2_code: str):
        """Sets the global_dimension2_code of this CountriesBody.

        The global dimension 2 code of the country  # noqa: E501

        :param global_dimension2_code: The global_dimension2_code of this CountriesBody.
        :type global_dimension2_code: str
        """

        self._global_dimension2_code = global_dimension2_code

    @property
    def customer_template_code(self) -> str:
        """Gets the customer_template_code of this CountriesBody.

        The customer template code of the country  # noqa: E501

        :return: The customer_template_code of this CountriesBody.
        :rtype: str
        """
        return self._customer_template_code

    @customer_template_code.setter
    def customer_template_code(self, customer_template_code: str):
        """Sets the customer_template_code of this CountriesBody.

        The customer template code of the country  # noqa: E501

        :param customer_template_code: The customer_template_code of this CountriesBody.
        :type customer_template_code: str
        """

        self._customer_template_code = customer_template_code

    @property
    def income_cost_carrier_code(self) -> str:
        """Gets the income_cost_carrier_code of this CountriesBody.

        The income cost carrier code of the country  # noqa: E501

        :return: The income_cost_carrier_code of this CountriesBody.
        :rtype: str
        """
        return self._income_cost_carrier_code

    @income_cost_carrier_code.setter
    def income_cost_carrier_code(self, income_cost_carrier_code: str):
        """Sets the income_cost_carrier_code of this CountriesBody.

        The income cost carrier code of the country  # noqa: E501

        :param income_cost_carrier_code: The income_cost_carrier_code of this CountriesBody.
        :type income_cost_carrier_code: str
        """

        self._income_cost_carrier_code = income_cost_carrier_code

    @property
    def eu_affiliation(self) -> str:
        """Gets the eu_affiliation of this CountriesBody.

        The EU affiliation of the country  # noqa: E501

        :return: The eu_affiliation of this CountriesBody.
        :rtype: str
        """
        return self._eu_affiliation

    @eu_affiliation.setter
    def eu_affiliation(self, eu_affiliation: str):
        """Sets the eu_affiliation of this CountriesBody.

        The EU affiliation of the country  # noqa: E501

        :param eu_affiliation: The eu_affiliation of this CountriesBody.
        :type eu_affiliation: str
        """

        self._eu_affiliation = eu_affiliation

    @property
    def continent(self) -> str:
        """Gets the continent of this CountriesBody.

        The continent of the country  # noqa: E501

        :return: The continent of this CountriesBody.
        :rtype: str
        """
        return self._continent

    @continent.setter
    def continent(self, continent: str):
        """Sets the continent of this CountriesBody.

        The continent of the country  # noqa: E501

        :param continent: The continent of this CountriesBody.
        :type continent: str
        """

        self._continent = continent

    @property
    def max_iban_length(self) -> str:
        """Gets the max_iban_length of this CountriesBody.

        The maximum length of the IBAN in the country  # noqa: E501

        :return: The max_iban_length of this CountriesBody.
        :rtype: str
        """
        return self._max_iban_length

    @max_iban_length.setter
    def max_iban_length(self, max_iban_length: str):
        """Sets the max_iban_length of this CountriesBody.

        The maximum length of the IBAN in the country  # noqa: E501

        :param max_iban_length: The max_iban_length of this CountriesBody.
        :type max_iban_length: str
        """

        self._max_iban_length = max_iban_length

    @property
    def length_of_bank_branch_code(self) -> str:
        """Gets the length_of_bank_branch_code of this CountriesBody.

        The length of the bank branch code in the country  # noqa: E501

        :return: The length_of_bank_branch_code of this CountriesBody.
        :rtype: str
        """
        return self._length_of_bank_branch_code

    @length_of_bank_branch_code.setter
    def length_of_bank_branch_code(self, length_of_bank_branch_code: str):
        """Sets the length_of_bank_branch_code of this CountriesBody.

        The length of the bank branch code in the country  # noqa: E501

        :param length_of_bank_branch_code: The length_of_bank_branch_code of this CountriesBody.
        :type length_of_bank_branch_code: str
        """

        self._length_of_bank_branch_code = length_of_bank_branch_code

    @property
    def responsibility_center(self) -> str:
        """Gets the responsibility_center of this CountriesBody.

        The responsibility center of the country  # noqa: E501

        :return: The responsibility_center of this CountriesBody.
        :rtype: str
        """
        return self._responsibility_center

    @responsibility_center.setter
    def responsibility_center(self, responsibility_center: str):
        """Sets the responsibility_center of this CountriesBody.

        The responsibility center of the country  # noqa: E501

        :param responsibility_center: The responsibility_center of this CountriesBody.
        :type responsibility_center: str
        """

        self._responsibility_center = responsibility_center

    @property
    def iso_code(self) -> str:
        """Gets the iso_code of this CountriesBody.

        The ISO code of the country  # noqa: E501

        :return: The iso_code of this CountriesBody.
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code: str):
        """Sets the iso_code of this CountriesBody.

        The ISO code of the country  # noqa: E501

        :param iso_code: The iso_code of this CountriesBody.
        :type iso_code: str
        """

        self._iso_code = iso_code

    @property
    def culture_info(self) -> str:
        """Gets the culture_info of this CountriesBody.

        The culture info of the country  # noqa: E501

        :return: The culture_info of this CountriesBody.
        :rtype: str
        """
        return self._culture_info

    @culture_info.setter
    def culture_info(self, culture_info: str):
        """Sets the culture_info of this CountriesBody.

        The culture info of the country  # noqa: E501

        :param culture_info: The culture_info of this CountriesBody.
        :type culture_info: str
        """

        self._culture_info = culture_info

    @property
    def signature(self) -> str:
        """Gets the signature of this CountriesBody.

        The signature of the country  # noqa: E501

        :return: The signature of this CountriesBody.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature: str):
        """Sets the signature of this CountriesBody.

        The signature of the country  # noqa: E501

        :param signature: The signature of this CountriesBody.
        :type signature: str
        """

        self._signature = signature

    @property
    def primary_language_code(self) -> str:
        """Gets the primary_language_code of this CountriesBody.

        The primary language code of the country  # noqa: E501

        :return: The primary_language_code of this CountriesBody.
        :rtype: str
        """
        return self._primary_language_code

    @primary_language_code.setter
    def primary_language_code(self, primary_language_code: str):
        """Sets the primary_language_code of this CountriesBody.

        The primary language code of the country  # noqa: E501

        :param primary_language_code: The primary_language_code of this CountriesBody.
        :type primary_language_code: str
        """

        self._primary_language_code = primary_language_code

    @property
    def bank_country_code(self) -> str:
        """Gets the bank_country_code of this CountriesBody.

        The bank country code of the country  # noqa: E501

        :return: The bank_country_code of this CountriesBody.
        :rtype: str
        """
        return self._bank_country_code

    @bank_country_code.setter
    def bank_country_code(self, bank_country_code: str):
        """Sets the bank_country_code of this CountriesBody.

        The bank country code of the country  # noqa: E501

        :param bank_country_code: The bank_country_code of this CountriesBody.
        :type bank_country_code: str
        """

        self._bank_country_code = bank_country_code

    @property
    def eu_standard(self) -> str:
        """Gets the eu_standard of this CountriesBody.

        The EU standard of the country  # noqa: E501

        :return: The eu_standard of this CountriesBody.
        :rtype: str
        """
        return self._eu_standard

    @eu_standard.setter
    def eu_standard(self, eu_standard: str):
        """Sets the eu_standard of this CountriesBody.

        The EU standard of the country  # noqa: E501

        :param eu_standard: The eu_standard of this CountriesBody.
        :type eu_standard: str
        """

        self._eu_standard = eu_standard

    @property
    def invoicing_in_local_currency(self) -> str:
        """Gets the invoicing_in_local_currency of this CountriesBody.

        Indicates if invoicing is done in the local currency of the country  # noqa: E501

        :return: The invoicing_in_local_currency of this CountriesBody.
        :rtype: str
        """
        return self._invoicing_in_local_currency

    @invoicing_in_local_currency.setter
    def invoicing_in_local_currency(self, invoicing_in_local_currency: str):
        """Sets the invoicing_in_local_currency of this CountriesBody.

        Indicates if invoicing is done in the local currency of the country  # noqa: E501

        :param invoicing_in_local_currency: The invoicing_in_local_currency of this CountriesBody.
        :type invoicing_in_local_currency: str
        """

        self._invoicing_in_local_currency = invoicing_in_local_currency

    @property
    def currency_code(self) -> str:
        """Gets the currency_code of this CountriesBody.

        The currency code of the country  # noqa: E501

        :return: The currency_code of this CountriesBody.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code: str):
        """Sets the currency_code of this CountriesBody.

        The currency code of the country  # noqa: E501

        :param currency_code: The currency_code of this CountriesBody.
        :type currency_code: str
        """

        self._currency_code = currency_code

    @property
    def default_length_branch_code(self) -> str:
        """Gets the default_length_branch_code of this CountriesBody.

        The default length of the branch code in the country  # noqa: E501

        :return: The default_length_branch_code of this CountriesBody.
        :rtype: str
        """
        return self._default_length_branch_code

    @default_length_branch_code.setter
    def default_length_branch_code(self, default_length_branch_code: str):
        """Sets the default_length_branch_code of this CountriesBody.

        The default length of the branch code in the country  # noqa: E501

        :param default_length_branch_code: The default_length_branch_code of this CountriesBody.
        :type default_length_branch_code: str
        """

        self._default_length_branch_code = default_length_branch_code

    @property
    def default_length_account_no(self) -> str:
        """Gets the default_length_account_no of this CountriesBody.

        The default length of the account number in the country  # noqa: E501

        :return: The default_length_account_no of this CountriesBody.
        :rtype: str
        """
        return self._default_length_account_no

    @default_length_account_no.setter
    def default_length_account_no(self, default_length_account_no: str):
        """Sets the default_length_account_no of this CountriesBody.

        The default length of the account number in the country  # noqa: E501

        :param default_length_account_no: The default_length_account_no of this CountriesBody.
        :type default_length_account_no: str
        """

        self._default_length_account_no = default_length_account_no

    @property
    def iso_bank_code(self) -> str:
        """Gets the iso_bank_code of this CountriesBody.

        The ISO bank code of the country  # noqa: E501

        :return: The iso_bank_code of this CountriesBody.
        :rtype: str
        """
        return self._iso_bank_code

    @iso_bank_code.setter
    def iso_bank_code(self, iso_bank_code: str):
        """Sets the iso_bank_code of this CountriesBody.

        The ISO bank code of the country  # noqa: E501

        :param iso_bank_code: The iso_bank_code of this CountriesBody.
        :type iso_bank_code: str
        """

        self._iso_bank_code = iso_bank_code

    @property
    def accounting_period(self) -> str:
        """Gets the accounting_period of this CountriesBody.

        The accounting period of the country  # noqa: E501

        :return: The accounting_period of this CountriesBody.
        :rtype: str
        """
        return self._accounting_period

    @accounting_period.setter
    def accounting_period(self, accounting_period: str):
        """Sets the accounting_period of this CountriesBody.

        The accounting period of the country  # noqa: E501

        :param accounting_period: The accounting_period of this CountriesBody.
        :type accounting_period: str
        """

        self._accounting_period = accounting_period

    @property
    def vat_registration_obligation(self) -> str:
        """Gets the vat_registration_obligation of this CountriesBody.

        The VAT registration obligation of the country  # noqa: E501

        :return: The vat_registration_obligation of this CountriesBody.
        :rtype: str
        """
        return self._vat_registration_obligation

    @vat_registration_obligation.setter
    def vat_registration_obligation(self, vat_registration_obligation: str):
        """Sets the vat_registration_obligation of this CountriesBody.

        The VAT registration obligation of the country  # noqa: E501

        :param vat_registration_obligation: The vat_registration_obligation of this CountriesBody.
        :type vat_registration_obligation: str
        """

        self._vat_registration_obligation = vat_registration_obligation

    @property
    def vend_gen_bus_posting_group(self) -> str:
        """Gets the vend_gen_bus_posting_group of this CountriesBody.

        The vendor general business posting group of the country  # noqa: E501

        :return: The vend_gen_bus_posting_group of this CountriesBody.
        :rtype: str
        """
        return self._vend_gen_bus_posting_group

    @vend_gen_bus_posting_group.setter
    def vend_gen_bus_posting_group(self, vend_gen_bus_posting_group: str):
        """Sets the vend_gen_bus_posting_group of this CountriesBody.

        The vendor general business posting group of the country  # noqa: E501

        :param vend_gen_bus_posting_group: The vend_gen_bus_posting_group of this CountriesBody.
        :type vend_gen_bus_posting_group: str
        """

        self._vend_gen_bus_posting_group = vend_gen_bus_posting_group

    @property
    def cust_gen_bus_posting_group(self) -> str:
        """Gets the cust_gen_bus_posting_group of this CountriesBody.

        The customer general business posting group of the country  # noqa: E501

        :return: The cust_gen_bus_posting_group of this CountriesBody.
        :rtype: str
        """
        return self._cust_gen_bus_posting_group

    @cust_gen_bus_posting_group.setter
    def cust_gen_bus_posting_group(self, cust_gen_bus_posting_group: str):
        """Sets the cust_gen_bus_posting_group of this CountriesBody.

        The customer general business posting group of the country  # noqa: E501

        :param cust_gen_bus_posting_group: The cust_gen_bus_posting_group of this CountriesBody.
        :type cust_gen_bus_posting_group: str
        """

        self._cust_gen_bus_posting_group = cust_gen_bus_posting_group

    @property
    def tenant(self) -> str:
        """Gets the tenant of this CountriesBody.

        The tenant name  # noqa: E501

        :return: The tenant of this CountriesBody.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant: str):
        """Sets the tenant of this CountriesBody.

        The tenant name  # noqa: E501

        :param tenant: The tenant of this CountriesBody.
        :type tenant: str
        """

        self._tenant = tenant
