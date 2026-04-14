from dataclasses import dataclass


@dataclass
class ConflictResolver:
    default_priority: dict[str, int]

    def resolve(self, options: dict[str, float]) -> str:
        ranked = sorted(
            options.items(),
            key=lambda item: (item[1], self.default_priority.get(item[0], 0)),
            reverse=True,
        )
        return ranked[0][0]
