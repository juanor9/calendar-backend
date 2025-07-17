import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello Tanuki 🦝"


schema = strawberry.Schema(query=Query)
