/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   __variance.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yhetman <yhetman@student.unit.ua>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/29 18:20:58 by yhetman           #+#    #+#             */
/*   Updated: 2020/03/29 18:22:05 by yhetman          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#include "poisson_simulation.h"

double __variance(int n, int vec[])
{
	int		i;
	double	mean;
	double	variance;

	if (n < 2)
		variance = 0.0;
	else
	{
		mean = __mean(n, vec);
		variance = 0.0;
		for ( i = 0; i < n; i++ )
			variance += pow(((double) vec[i] - mean), 2);
		variance /= (double)(n - 1);
	}
    return (variance);
}
