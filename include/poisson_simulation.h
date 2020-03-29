/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   poisson_simulation.h                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yhetman <yhetman@student.unit.ua>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/29 12:42:37 by yhetman           #+#    #+#             */
/*   Updated: 2020/03/29 18:24:01 by yhetman          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef POISSON_SIMULATION_H
# define POISSON_SIMULATION_H

# define MIN(X, Y)	(((X) < (Y)) ? (X) : (Y))

void	timestamp(void);

double	__mean(int n, int vec[]);
double	__variance(int n, int vec[]);
#endif
