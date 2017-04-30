(define (domain rovers)
	(:requirements :fluents :durative-actions :typing )
	(:types
		rover pos - object
		)
	(:functions
		(x ?r - object)
		)

	(:predicates
		(idle ?r - rover)
		(at ?r - rover ?p - pos)
		(next ?p1 - pos ?p2 - pos)
		(empty ?p - pos)
		)

	(:durative-action move
		:parameters (?r - rover ?p1 - pos ?p2 - pos)
		:duration (= ?duration 1)
		:condition (and
			(at start (empty ?p2))
			(at start (idle ?r))
			(at start (at ?r ?p1))
			(at start (next ?p1 ?p2))
			)
		:effect	(and
			(at start (not (idle ?r)))
			(at end (idle ?r))
			(at start (not (at ?r ?p1)))
			(at end (at ?r ?p2))
			)
		)

	)
