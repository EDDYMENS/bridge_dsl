from dsl import Rules

business_type = 'enterprise'
company_name = 'interflix'

rules = Rules();

rules. \
    on_query().whenever(business_type == "enterprise").run('Accounts', 'account_type', [company_name]) \
    .whenever(rules.results == "premium")\
    .run('ChargeRate', 'allow_discount', [3.0])


print rules.results
